## Como rodar

Execute o arquivo install.sh
```
    chmod +x install.sh
    ./install.sh
```

Alternativamente você pode rodar os comandos manualmente
```
    pip3 install -e .

    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Se necessario, adcione o caminho onde o script ds está instalado ao PATH (provavelmente estara em algo como /home/.../.local/bin)
```
    export PATH=$PATH:/caminho/para/o/script
```

A CLI precisa também de credenciais da Google, para isso você pode seguir o passo-a-passo [Como criar um projeto Google Cloud](https://developers.google.com/workspace/guides/create-project) e então [Como criar Credenciais de acesso](https://developers.google.com/workspace/guides/create-credentials#desktop-app) para criar um ID de Cliente.

Com o ID de cliente criado, basta baixa-lo, renomear para 'credentials.json' e mover para a pasta raiz do projeto.

Por fim, crie um arquivo com o nome "folder_resgister.txt" na raiz do projeto.


Agora você conseguirá usar os comandos ds no seu console (o console precisa rodar na pasta do projeto).

A primeira vez que rodar qualquer comando você será redirecionado para a autenticação da conta do google, logue na conta da qual deseja usar o drive.


## Comandos em desenvolvimento:

   - [x] ds list (mostar os 10 primeiros arquivos do qual o drive tem acesso)

   - [x] ds up (upa um arquivo para o drive)

   - [ ] ds sync (sincroniza uma pasta com o drive para fazer backup automatico)

   P.S.: Atualmente o comando sync funciona apenas para upar uma pasta(incluindo tudo que há nela) para o Google Drive
