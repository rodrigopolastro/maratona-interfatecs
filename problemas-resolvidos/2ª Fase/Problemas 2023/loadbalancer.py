def clean_servers(req_instant):
  for i in range(n_servers):
    servers[i] = list(filter(lambda req : req >= req_instant, servers[i]))

def destiny_server():
  least_n_load = len(servers[0])
  server_index = 0
  for i in range(1,n_servers):
    server_n_requests = len(servers[i])
    if server_n_requests < least_n_load:
      least_n_load = server_n_requests
      server_index = i

  return server_index

requests = []

n_servers  = int(input())
servers = [[]] * n_servers

n_requests = int(input())
informed_req = int(input())
for i in range(n_requests): 
  request = input().split(' ')
  instant  = int(request[0])
  duration = int(request[1])
  requests.append([instant, duration])

informed_req_instant = requests[informed_req - 1][0]
requests.sort()

#====== VERSION 1 ======

# requests = list(filter(lambda req : req[0] <= informed_req_instant, requests))
# for i in range(len(requests)):
#   req = requests[i]
#   req_last_instant = req[0] + req[1] - 1
#   clean_servers(req[0])
#   server_index = destiny_server()
#   servers[server_index] = servers[server_index] + [req_last_instant]
#   if i == len(requests)-1: 
#     print(server_index + 1)

#====== VERSION 2 ======

for i in range(len(requests)):
  req = requests[i]
  req_last_instant = req[0] + req[1] - 1
  clean_servers(req[0])
  server_index = destiny_server()
  if(req[0] == informed_req_instant):
    print(server_index + 1)
    break
  servers[server_index] = servers[server_index] + [req_last_instant]

