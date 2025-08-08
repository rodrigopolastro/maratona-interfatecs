#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import shutil
from io import StringIO
from importlib import import_module
from pathlib import Path
from typing import List, Optional


class TestRunner:
    """Classe responsável por executar testes automáticos de exercícios."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.programa_dir = self.base_dir / "programa"
        self.exercise_dir = self.base_dir / "exercise"
        self.correct_count = 0

    def find_python_file(self, directory: Path) -> Optional[str]:
        """Encontra o primeiro arquivo Python no diretório especificado."""
        try:
            for file in directory.iterdir():
                if file.is_file() and file.suffix == '.py':
                    return file.stem
        except FileNotFoundError:
            pass
        return None

    def find_exercise_directory(self, exercise_name: str) -> Optional[Path]:
        """Encontra o diretório do exercício baseado no nome."""
        if not self.exercise_dir.exists():
            return None

        for exercise_path in self.exercise_dir.iterdir():
            if not exercise_path.is_dir():
                continue

            # Verifica se o nome do exercício está após o underscore
            parts = exercise_path.name.split('_')
            if len(parts) > 1 and parts[1] == exercise_name:
                return exercise_path
            # Verifica se o nome é exato
            elif exercise_path.name == exercise_name:
                return exercise_path

        return None

    def extract_number(self, filename: str) -> int:
        """Extrai o número de um nome de arquivo."""
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else 0

    def sort_files(self, files: List[str]) -> List[str]:
        """Ordena arquivos baseado nos números contidos nos nomes."""
        return sorted(files, key=self.extract_number)

    def clean_output(self, text: str) -> List[str]:
        """Limpa e formata a saída removendo espaços e quebras de linha desnecessárias."""
        lines = text.strip().split('\n')
        return [line.strip() for line in lines if line.strip()]

    def get_test_files(self, exercise_path: Path) -> tuple[List[str], List[str]]:
        """Obtém e ordena os arquivos de entrada e saída."""
        input_dir = exercise_path / "in"
        output_dir = exercise_path / "out"

        if not input_dir.exists() or not output_dir.exists():
            raise FileNotFoundError(f"Diretórios de teste não encontrados em {exercise_path}")

        input_files = [f.name for f in input_dir.iterdir() if f.is_file()]
        output_files = [f.name for f in output_dir.iterdir() if f.is_file()]

        return self.sort_files(input_files), self.sort_files(output_files)

    def run_single_test(self, module_name: str, input_file: Path, output_file: Path) -> bool:
        """Executa um único teste e retorna se passou ou não."""
        # Salva os streams originais
        original_stdin = sys.stdin
        original_stdout = sys.stdout

        try:
            # Lê a saída esperada
            with open(output_file, 'r', encoding='utf-8') as f:
                expected_output = self.clean_output(f.read())

            # Configura a entrada e captura a saída
            with open(input_file, 'r', encoding='utf-8') as f:
                sys.stdin = f
                captured_output = StringIO()
                sys.stdout = captured_output

                # Remove o módulo do cache se já foi importado
                if module_name in sys.modules:
                    del sys.modules[module_name]

                # Executa o programa
                import_module(module_name)

                # Obtém a saída capturada
                actual_output = self.clean_output(captured_output.getvalue())

            # Compara as saídas
            if actual_output == expected_output:
                return True
            else:
                self.print_diff(actual_output, expected_output, input_file.name)
                return False

        except Exception as e:
            print(f"Erro ao executar teste {input_file.name}: {e}")
            return False
        finally:
            # Restaura os streams originais
            sys.stdin = original_stdin
            sys.stdout = original_stdout

    def print_diff(self, actual: List[str], expected: List[str], test_name: str):
        """Imprime as diferenças entre a saída atual e esperada."""
        print(f"\n❌ ERRO no teste {test_name}:")
        print("Saída obtida:")
        for i, line in enumerate(actual, 1):
            print(f"  {i}: '{line}'")
        print("Saída esperada:")
        for i, line in enumerate(expected, 1):
            print(f"  {i}: '{line}'")

        # Mostra diferenças linha por linha
        max_lines = max(len(actual), len(expected))
        for i in range(max_lines):
            actual_line = actual[i] if i < len(actual) else "<linha ausente>"
            expected_line = expected[i] if i < len(expected) else "<linha ausente>"
            if actual_line != expected_line:
                print(f"  Diferença na linha {i+1}: '{actual_line}' ≠ '{expected_line}'")

    def cleanup_cache(self):
        """Remove arquivos de cache do Python."""
        cache_dir = self.programa_dir / "__pycache__"
        if cache_dir.exists():
            try:
                shutil.rmtree(cache_dir)
            except Exception:
                pass

    def run_tests(self) -> bool:
        """Executa todos os testes para o exercício encontrado."""
        print("🚀 Iniciando sistema de testes...\n")

        # Verifica se o diretório programa existe
        if not self.programa_dir.exists():
            print("❌ Erro: Diretório 'programa' não encontrado.")
            print("   Crie o diretório e coloque seu arquivo .py dentro dele.")
            return False

        # Encontra o arquivo Python
        python_file = self.find_python_file(self.programa_dir)
        if not python_file:
            print("❌ Erro: Nenhum arquivo .py encontrado no diretório 'programa'.")
            return False

        print(f"📁 Arquivo encontrado: {python_file}.py")

        # Encontra o diretório do exercício
        exercise_path = self.find_exercise_directory(python_file)
        if not exercise_path:
            print(f"❌ Erro: Diretório do exercício '{python_file}' não encontrado.")
            print("   Verifique se o nome do arquivo corresponde ao exercício.")
            return False

        print(f"📂 Exercício encontrado: {exercise_path.name}")

        try:
            # Obtém os arquivos de teste
            input_files, output_files = self.get_test_files(exercise_path)

            if len(input_files) != len(output_files):
                print("⚠️  Aviso: Número de arquivos de entrada e saída não coincidem.")

            total_tests = min(len(input_files), len(output_files))
            print(f"🧪 Executando {total_tests} testes...\n")

            # Executa os testes
            module_name = f"programa.{python_file}"

            for i in range(total_tests):
                input_file = exercise_path / "in" / input_files[i]
                output_file = exercise_path / "out" / output_files[i]

                print(f"Teste {i+1}/{total_tests}: {input_files[i]}... ", end="")

                if self.run_single_test(module_name, input_file, output_file):
                    print("✅ PASSOU")
                    self.correct_count += 1
                else:
                    print("❌ FALHOU")

            # Resultado final
            print(f"\n{'='*50}")
            if self.correct_count == total_tests:
                print(f"🎉 PARABÉNS! Todos os {total_tests} testes passaram!")
                print("✅ CORRECT ANSWER")
                return True
            else:
                print(f"📊 Resultado: {self.correct_count}/{total_tests} testes passaram")
                print("❌ WRONG ANSWER")
                return False

        except Exception as e:
            print(f"❌ Erro durante a execução dos testes: {e}")
            return False
        finally:
            self.cleanup_cache()


def main():
    """Função principal do programa."""
    try:
        runner = TestRunner()
        success = runner.run_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️  Execução interrompida pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
