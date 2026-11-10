# Atividade 4 — Testes Automatizados do LocalEats

Trabalho individual de Qualidade de Software.

Acesse a pasta `atividades/atividade-04` para visualizar a atividade em Markdown, os testes e o relatório.

## Como executar

No PowerShell, a partir da pasta `atividades/atividade-04`:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

O teste funcional precisa de acesso à internet para abrir o LocalEats.
