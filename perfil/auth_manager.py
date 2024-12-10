class AuthManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthManager, cls).__new__(cls)
            cls._instance.reset()
        return cls._instance

    def login(self, request, usuario):
        """Autentica o usuário e salva as informações na sessão."""
        self.usuario_id = usuario.id
        self.nome_completo = usuario.nome_completo
        self.email = usuario.email
        self.tipo_usuario = usuario.tipo_usuario
        self.is_authenticated = True

        # Salvar informações na sessão
        request.session['usuario_id'] = self.usuario_id
        request.session['nome_completo'] = self.nome_completo
        request.session['email'] = self.email
        request.session['tipo_usuario'] = self.tipo_usuario

    def logout(self, request):
        """Remove as informações de autenticação."""
        self.reset()
        request.session.flush()

    def reset(self):
        """Reseta as informações de autenticação."""
        self.usuario_id = None
        self.nome_completo = None
        self.email = None
        self.tipo_usuario = None
        self.is_authenticated = False

    def get_user_info(self, request):
        """Retorna informações do usuário, sincronizando com a sessão."""
        self.usuario_id = request.session.get('usuario_id')
        self.nome_completo = request.session.get('nome_completo')
        self.email = request.session.get('email')
        self.tipo_usuario = request.session.get('tipo_usuario')
        self.is_authenticated = self.usuario_id is not None

        return {
            "id": self.usuario_id,
            "nome_completo": self.nome_completo,
            "email": self.email,
            "tipo_usuario": self.tipo_usuario,
            "is_authenticated": self.is_authenticated,
        }
