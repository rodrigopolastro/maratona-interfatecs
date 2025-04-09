entrada = [int(x) for x in input().split()]
maiorComparacao = max(entrada)
if entrada[0] == entrada[1]:
    print('ERRO')
else:
    if (abs(entrada[0]) ==maiorComparacao and abs(entrada[1]) == maiorComparacao-1) or (abs(entrada[1])==maiorComparacao and abs(entrada[0]) == maiorComparacao-1):
        print('ERRO')
    elif (entrada[0] % entrada[1] != 0) and (entrada[1] % entrada[0] != 0):
        print("ERRO")
    else:
        # for _ in range(8):
        #     print(entrada[0],entrada[1])
        #     if(entrada[0] > entrada[1]):
        #         if entrada[1] < 0 and entrada[0] < 0:
        #             entrada = [entrada[1], entrada[0]]
        #         elif entrada[1] > 0 and entrada[0] > 0:
        #             entrada = [entrada[1],entrada[0]]
        #         elif entrada[1] < 0:
        #             entrada = [-entrada[1], -entrada[0]]
        #         else:
        #             entrada = [entrada[0], -entrada[1]]
        #     elif(entrada[0] < entrada[1]):
        #         if entrada[0] < entrada[1] and entrada[1] <0 and entrada[0] <0: #
        #             entrada = [entrada[0], -entrada[1]]
        #         elif entrada[0] < entrada[1] and entrada[1] <0: #
        #             entrada = [-entrada[0],entrada[1]]
        #         elif entrada[0] < entrada[1] and entrada[1]> 0 and entrada[0] < 0: #
        #             entrada = [-entrada[1],-entrada[0]]
        #         else:
        #             entrada = [entrada[1],entrada[0]]
        print(entrada[0],entrada[1])
        print(entrada[1],entrada[0])
        print(entrada[1],-entrada[0])
        print(entrada[0],-entrada[1])
        print(-entrada[0],-entrada[1])
        print(-entrada[1],-entrada[0])
        print(-entrada[1],entrada[0])
        print(-entrada[0],entrada[1])
        
                    
       

                
            
            
