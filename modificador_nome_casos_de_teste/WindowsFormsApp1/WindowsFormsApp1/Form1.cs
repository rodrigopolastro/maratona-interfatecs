using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnConverter_Click(object sender, EventArgs e)
        {
            string caminhoArquivo = txtCaminhoArquivo.Text;
            errorProvider1.SetError(txtCaminhoArquivo, string.Empty);
            if (string.IsNullOrWhiteSpace(caminhoArquivo))
            {
                errorProvider1.SetError(txtCaminhoArquivo, "Insira um caminho para arquivo");
                return;
            }
            if (MessageBox.Show("Deseja refatorar os nomes dos arquivos (retirando todas letras, deixando apenas os números da pasta " + txtCaminhoArquivo + "?", "Confirmação", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                string[] arquivos = Directory.GetFiles(caminhoArquivo);
                if (arquivos.Length == 0)
                {
                    MessageBox.Show("Não encontrado arquivos na pasta, verifique o caminho");
                    return;
                }
                int arquivosModificados = 0;
                foreach (var caminhoOriginal in arquivos)
                {
                    string nomeArquivo = Path.GetFileNameWithoutExtension(caminhoOriginal);
                    string extensao = Path.GetExtension(caminhoOriginal);
                    string pastaPai = Path.GetDirectoryName(caminhoOriginal);

                    // Se o nome contém pelo menos um dígito
                    if (Regex.IsMatch(nomeArquivo, @"\d"))
                    {
                        // Remove tudo que não for dígito
                        string novoNome = new string(nomeArquivo.Where(char.IsDigit).ToArray()) + extensao;
                        string caminhoNovo = Path.Combine(pastaPai, novoNome);

                        if (string.Equals(caminhoNovo, caminhoOriginal, StringComparison.OrdinalIgnoreCase))
                        {
                            continue;
                        }

                        // Se o novo nome já existir, comparar o conteúdo
                        if (File.Exists(caminhoNovo))
                        {
                            bool conteudoIgual = FileEquals(caminhoOriginal, caminhoNovo);
                            if (conteudoIgual)
                            {
                                File.Delete(caminhoOriginal);
                            }
                        }
                        else
                        {
                            File.Move(caminhoOriginal, caminhoNovo);
                        }
                        arquivosModificados++;
                    }

                }

                if (arquivosModificados > 0)
                {
                    MessageBox.Show($"{arquivosModificados}/{arquivos.Length} arquivos foram modificados", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    MessageBox.Show($"Houve algum erro, verifique os arquivos", "Falha grave", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }

            }

        }

        private bool FileEquals(string caminho1, string caminho2)
        {
            byte[] file1 = File.ReadAllBytes(caminho1);
            byte[] file2 = File.ReadAllBytes(caminho2);
            return file1.SequenceEqual(file2);
        }
        private void btnProcurarPasta_Click(object sender, EventArgs e)
        {
            using(var fd = new FolderBrowserDialog())
            {
                if(!string.IsNullOrWhiteSpace(txtCaminhoArquivo.Text) && Directory.Exists(txtCaminhoArquivo.Text))
                {
                    fd.SelectedPath = txtCaminhoArquivo.Text;
                }
                if(fd.ShowDialog() != DialogResult.Cancel)
                {
                    string caminhoArquivo = fd.SelectedPath;

                    txtCaminhoArquivo.Text = caminhoArquivo;


                }
                
            }
        }
    }
}
