import requests
import json

def get_mrs(project_id :int, state :str, username :str):
  mrs = requests.get(
          f"https://gitlab.com/api/v4/projects/{project_id}/merge_requests?state={state}&author_username={username}"
        )
  return mrs.json()

if __name__ == '__main__':
  project_id = int(input("Insira o id do projeto: "))
  state = input("Insira o estado do merge request (opened, closed, merged, all): ")
  username = input("Insira o nome do usuário: ")
  user_mrs = []
  mrs = get_mrs(project_id, state, username)

  for mr in mrs:
    user_mrs.append({
      "id": mr["id"],
      "reference": mr["reference"],
      "title": mr["title"],
      "description": mr["description"]
    })

  with open("./files/user_mrs.json", "w") as arquivo:
    json.dump(user_mrs, arquivo, indent=4)
