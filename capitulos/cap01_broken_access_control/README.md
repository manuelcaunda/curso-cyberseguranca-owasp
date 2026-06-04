# 🔓 Capítulo 1: Broken Access Control (Controlo de Acesso Quebrado)

## 📖 Índice
1. [Introdução](#introdução)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Tipos de Broken Access Control](#tipos-de-broken-access-control)
4. [Exemplos Vulneráveis](#exemplos-vulneráveis)
5. [Código Seguro](#código-seguro)
6. [Exercícios Práticos](#exercícios-práticos)
7. [Tarefas Guiadas](#tarefas-guiadas)
8. [Ferramentas](#ferramentas)

---

## 🎯 Introdução

**Broken Access Control** é a vulnerabilidade **#1 do OWASP Top 10 2021** e refere-se à falha em implementar corretamente mecanismos que verificam se um utilizador tem permissão para aceder a um recurso específico.

### Estatísticas
- Afeta **94%** das aplicações testadas
- Impacto: Acesso não autorizado a dados sensíveis
- Severidade: **Crítica**

---

## 📚 Conceitos Fundamentais

### O que é Controlo de Acesso?

Controlo de Acesso é o mecanismo que **autoriza** quem pode fazer o quê numa aplicação.

**Três elementos principais:**

1. **Autenticação (AuthN)** - Verificar QUEM é o utilizador
   - Login, senha, autenticação multi-fator
   
2. **Autorização (AuthZ)** - Verificar O QUÊ o utilizador pode fazer
   - Permissões, roles, políticas de acesso

3. **Auditoria** - Registar quem fez o quê
   - Logs de acesso, auditoria

### Diferença entre Autenticação e Autorização

```
┌─────────────────────────────────────────┐
│         Utilizador: João               │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │ AUTENTICAÇÃO        │
        │ "Você é João?"      │
        │ ✓ Senha correta     │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────────────┐
        │ AUTORIZAÇÃO                 │
        │ "Pode ver relatórios?"      │
        │ ✓ Tem role Admin?           │
        │ ✗ Sem permissão de vendas   │
        └─────────────────────────────┘
```

---

## 🔓 Tipos de Broken Access Control

### 1. **Horizontal Privilege Escalation (HPE)**
Um utilizador acede aos dados de outro utilizador no mesmo nível.

```
User A (ID: 1) ──(acesso não autorizado)──> User B (ID: 2) dados
```

**Exemplo**: Ver perfil de outro utilizador alterando o ID na URL.

### 2. **Vertical Privilege Escalation (VPE)**
Um utilizador com baixos privilégios acede a funcionalidades de administrador.

```
Utilizador Normal ──(acesso não autorizado)──> Painel Admin
```

**Exemplo**: Um utilizador comum acede ao painel administrativo.

### 3. **Insecure Direct Object References (IDOR)**
Acesso direto a objetos sem validação de permissões.

```
/user/profile?id=1 ──> Pode ver user 1
/user/profile?id=2 ──> Pode ver user 2 (não deveria)
```

### 4. **Path Traversal + Access Control**
Navegar entre diretórios protegidos.

### 5. **Metadata Manipulation**
Manipular cookies, tokens ou parâmetros ocultos para ganhar acesso.

---

## 💻 Exemplos Vulneráveis

Veja os ficheiros `vulneravel_*.py` neste diretório para exemplos práticos.

### Resumo das Vulnerabilidades:

1. **IDOR em Perfil de Utilizador** - `vulneravel_idor.py`
2. **Horizontal Access** - `vulneravel_horizontal.py`
3. **Vertical Escalation** - `vulneravel_vertical.py`
4. **URL Parameter Manipulation** - `vulneravel_url_param.py`

---

## ✅ Código Seguro

Veja os ficheiros `seguro_*.py` neste diretório para implementações seguras.

---

## 🎓 Exercícios Práticos

### Exercício 1: Identificar IDOR
**Dificuldade**: ⭐⭐

Dado um endpoint vulnerável, identifique como um atacante poderia aceder aos dados de outro utilizador.

### Exercício 2: Implementar Controlo de Acesso Baseado em Roles
**Dificuldade**: ⭐⭐⭐

Crie um sistema de permissões usando Python com diferentes níveis de acesso.

### Exercício 3: Encontrar Vertical Escalation
**Dificuldade**: ⭐⭐⭐⭐

Numa aplicação web vulnerável, escale privilégios de utilizador normal para admin.

---

## 🚀 Tarefas Guiadas

### Tarefa 1: Lab IDOR
**Objetivo**: Explorar uma vulnerabilidade IDOR numa aplicação Flask

**Tempo estimado**: 45 minutos

[Ir para Tarefa 1](./tarefas/tarefa01_idor_lab.md)

### Tarefa 2: Implementar Autorização Segura
**Objetivo**: Criar um sistema seguro de autorização

**Tempo estimado**: 60 minutos

[Ir para Tarefa 2](./tarefas/tarefa02_autorizacao_segura.md)

### Tarefa 3: Auditoria de Aplicação
**Objetivo**: Testar uma aplicação e identificar falhas de acesso

**Tempo estimado**: 90 minutos

[Ir para Tarefa 3](./tarefas/tarefa03_auditoria.md)

---

## 🛠️ Ferramentas

### Ferramentas de Teste
- **Burp Suite Community** - Intercepção e teste de aplicações web
- **OWASP ZAP** - Scanner de segurança automático
- **Postman** - Testes de API
- **cURL** - Testes via linha de comando

### Bibliotecas Python
- **Flask** - Framework web leve
- **Django** - Framework web completo
- **SQLAlchemy** - ORM seguro
- **Python-dotenv** - Gestão de variáveis de ambiente

---

## 📊 Resumo de Aprendizagem

Ao final deste capítulo, você será capaz de:
✅ Entender a diferença entre autenticação e autorização  
✅ Identificar 5+ tipos de broken access control  
✅ Explorar vulnerabilidades IDOR  
✅ Implementar controlo de acesso seguro em Python  
✅ Usar ferramentas de teste para identificar falhas  
✅ Documentar e comunicar achados de segurança  

---

**Pronto para começar? Veja o próximo ficheiro: `01_teoria_detalhada.md`**
