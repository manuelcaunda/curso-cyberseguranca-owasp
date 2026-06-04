# 🔐 PARTE 0: FUNDAMENTOS DE SEGURANÇA

## 📚 Índice Completo

### 📖 Módulos Teóricos
1. [01 - Criptografia Básica](./01_criptografia_basica.md) ⭐
2. [02 - Autenticação vs Autorização](./02_autenticacao_autorizacao.md) ⭐
3. [03 - Princípios de Segurança (CIA)](./03_principios_seguranca.md) ⭐
4. [04 - Ferramentas Essenciais](./04_ferramentas_essenciais.md) ⭐

### 💻 Código Executável
- [exemplos_criptografia.py](./exemplos_criptografia.py) - 7 Exemplos práticos
- [exemplos_autenticacao.py](./exemplos_autenticacao.py) - Sistema completo de auth

### 📝 Exercícios & Desafios
- [exercicios.md](./exercicios.md) - 5 Exercícios com testes

---

## 🎯 Objetivos desta Parte

Ao completar os FUNDAMENTOS, você será capaz de:

✅ **Criptografia**
- [ ] Entender criptografia simétrica vs assimétrica
- [ ] Implementar hash seguro de senhas
- [ ] Usar Fernet para encriptação de dados
- [ ] Gerar e usar chaves RSA

✅ **Autenticação**
- [ ] Implementar sistema de login seguro
- [ ] Criar tokens de sessão
- [ ] Proteger contra força bruta
- [ ] Implementar MFA (conceito)

✅ **Autorização**
- [ ] Implementar RBAC (Role-Based Access Control)
- [ ] Criar políticas de acesso
- [ ] Auditar tentativas de acesso
- [ ] Implementar princípio de menor privilégio

✅ **Segurança Geral**
- [ ] Entender princípios CIA (Confidentiality, Integrity, Availability)
- [ ] Conhecer ferramentas essenciais
- [ ] Defender em profundidade
- [ ] Identificar ameaças com STRIDE

---

## 🚀 Como Usar Este Módulo

### **Dia 1-2: Criptografia**
```bash
# Ler teoria
cat 01_criptografia_basica.md

# Executar exemplos
python3 exemplos_criptografia.py

# Exercícios
cat exercicios.md  # Exercício 1-2
```

### **Dia 3-4: Autenticação**
```bash
# Ler teoria
cat 02_autenticacao_autorizacao.md

# Executar sistema
python3 exemplos_autenticacao.py

# Exercícios
cat exercicios.md  # Exercício 3
```

### **Dia 5: Princípios & Ferramentas**
```bash
# Ler teoria
cat 03_principios_seguranca.md
cat 04_ferramentas_essenciais.md

# Instalar ferramentas
sudo apt-get install burpsuite nmap wireshark

# Exercícios
cat exercicios.md  # Exercício 4-5
```

---

## 📊 Mapa de Progresso

```
┌────────────────────────────────────────────────────────────────────┐
│          FUNDAMENTOS DE SEGURANÇA                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  [████████░░░░░░░░] 40% - Criptografia            │
│  [░░░░░░░░░░░░░░░░░░] 0% - Autenticação           │
│  [░░░░░░░░░░░░░░░░░░] 0% - Autorização            │
│  [░░░░░░░░░░░░░░░░░░] 0% - Princípios & Tools     │
│                                                                    │
│  Total: █░░░░░░░░░░░░░░░░░ 10%                                   │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 🔒 Pré-requisitos

### Software Necessário
```bash
# Python 3.8+
python3 --version

# Pip (gestor de pacotes Python)
pip3 --version

# Git
git --version
```

### Instalar Dependências
```bash
pip install cryptography bcrypt argon2-cffi pyjwt flask requests paramiko
```

---

## 📋 Estrutura dos Módulos

Cada módulo segue este padrão:

```
📄 Módulo
 ├─ 📖 Teoria (com exemplos)
 ├─ 💻 Código Python executável
 ├─ 🧪 Exemplos práticos
 ├─ 📝 Exercícios com solução
 └─ 🔬 Laboratório prático
```

---

## 📚 Recursos Adicionais

### Documentação
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Cryptography.io Docs](https://cryptography.io/)
- [Python Security Best Practices](https://python.readthedocs.io/)

### Ferramentas Online
- [CyberChef](https://gchq.github.io/CyberChef/) - Encoding/Decoding
- [Hash Lookup](https://md5.gromweb.com/) - Hash Reversal
- [JWT.io](https://jwt.io/) - JWT Debugger

### Comunidades
- [OWASP Community](https://owasp.org/)
- [Reddit r/cybersecurity](https://reddit.com/r/cybersecurity/)
- [Stack Exchange Security](https://security.stackexchange.com/)

---

## ❓ Perguntas Frequentes

**P: Por onde começo?**
R: Comece por "01 - Criptografia Básica" e execute os exemplos.

**P: Quanto tempo leva?**
R: 1 semana dedicando 2-3 horas por dia.

**P: Preciso saber matemática avançada?**
R: Não! Focamos em implementação prática, não teoria matemática.

**P: Posso pular alguns tópicos?**
R: Recomendamos seguir sequência, mas cada módulo é independente.

---

## ✅ Checklist de Conclusão

Antes de passar para o Capítulo 1, confirme:

- [ ] Li toda teoria de criptografia
- [ ] Executei todos os exemplos sem erros
- [ ] Completei exercícios 1-2
- [ ] Li teoria de autenticação
- [ ] Completei exercício 3
- [ ] Li teoria de autorização
- [ ] Completei exercício 4
- [ ] Li princípios de segurança
- [ ] Instalei ferramentas básicas
- [ ] Completei exercício 5

---

## 🚀 Próximo Passo

Ao completar os FUNDAMENTOS, você estará pronto para:

**Capítulo 1: Broken Access Control** 🔒

Você aprenderá a:
- Identificar falhas de controlo de acesso
- Explorar vulnerabilidades de autorização
- Escalar privilégios
- Implementar controlo de acesso seguro

👉 [Começar Capítulo 1](../capitulos/cap01_broken_access_control/README.md)

---

**Status: Em Desenvolvimento Ativo** 🔄
**Última Atualização: 2026-06-04**
