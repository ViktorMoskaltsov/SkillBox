import os

def print_dir (project) :
    print('Содержимое ',project)
    for imn in os.listdir(project):
        path = os.path.join(project,imn)
        print('  ',path)






project_py = 'Python_Basic'


path_project = os.path.abspath(os.path.join('..','..',project_py))
print_dir(path_project)



