import os
import glob
import traceback
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

_NEEDED_COLS = ["FullName", "TeamName", "Position", "Points", "Year", "Date", "EventName"]
 
 
def _read_parquet(filepath: str) -> pd.DataFrame | None:

    try:
        df = pd.read_parquet(filepath, engine="fastparquet")
        cols = [c for c in _NEEDED_COLS if c in df.columns]
        return df[cols]
    except Exception:
        pass
 
    try:
        df = pd.read_parquet(filepath)
        cols = [c for c in _NEEDED_COLS if c in df.columns]
        return df[cols]
    except Exception as err:
        print(f"[DATA] Erro ao ler {os.path.basename(filepath)}: {err}")
        return None
 
 
def _load_all_races() -> pd.DataFrame:
    """Lê todos os arquivos *_R.parquet e retorna um DataFrame único."""
    print(f"[DATA] Procurando arquivos em: {DATA_DIR}")
 
    if not os.path.isdir(DATA_DIR):
        print(f"[DATA] ERRO: pasta 'data/' não encontrada em {DATA_DIR}")
        print("[DATA] Verifique se os arquivos .parquet estão na pasta correta.")
        return pd.DataFrame()
 
    files = sorted(glob.glob(os.path.join(DATA_DIR, "*_R.parquet")))
 
    if not files:
        print("[DATA] ERRO: nenhum arquivo *_R.parquet encontrado!")
        return pd.DataFrame()
 
    print(f"[DATA] {len(files)} arquivos encontrados. Carregando...")
 
    dfs = []
    failed = 0
    for i, f in enumerate(files):
        df = _read_parquet(f)
        if df is not None:
            dfs.append(df)
        else:
            failed += 1
 
        if (i + 1) % 100 == 0 or (i + 1) == len(files):
            print(f"[DATA]   {i + 1}/{len(files)} arquivos processados...")
 
    if failed > 0:
        print(f"[DATA] Aviso: {failed} arquivo(s) não puderam ser lidos.")
 
    if not dfs:
        print("[DATA] ERRO: nenhum arquivo foi carregado com sucesso.")
        return pd.DataFrame()
 
    result = pd.concat(dfs, ignore_index=True)
    print(f"[DATA] Carregamento concluído: {len(result)} registros.")
    return result
 
 
def _points_leaders_per_year(df: pd.DataFrame) -> str:
    """Piloto com mais pontos acumulados em cada temporada."""
    leaders = (
        df.groupby(["Year", "FullName"])["Points"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Points"], ascending=[True, False])
        .drop_duplicates("Year")
    )
    return "\n".join(
        f"  {int(r.Year)}: {r.FullName} ({r.Points:.0f} pts)"
        for r in leaders.itertuples()
    )
 
 
def build_data_context() -> str:

    print("[DATA] Carregando dados históricos de F1...")
 
    try:
        df = _load_all_races()
    except Exception:
        print("[DATA] ERRO inesperado ao carregar dados:")
        traceback.print_exc()
        return "Dados históricos de corridas não disponíveis no momento."
 
    if df.empty:
        return "Dados históricos de corridas não disponíveis no momento."
 
    try:
        winners = df[df["Position"] == 1.0].copy()
        all_years = sorted(df["Year"].unique())
        last_two = all_years[-2:]
 
        top_drivers = winners["FullName"].value_counts().head(15)
        driver_wins_str = "\n".join(
            f"  {name}: {count} vitórias" for name, count in top_drivers.items()
        )
 
        top_teams = winners["TeamName"].value_counts().head(10)
        team_wins_str = "\n".join(
            f"  {name}: {count} vitórias" for name, count in top_teams.items()
        )
 
        champ_str = _points_leaders_per_year(df)
 
        recent_races = winners.sort_values("Date").tail(10)[
            ["Year", "EventName", "FullName", "TeamName"]
        ]
        recent_str = "\n".join(
            f"  {int(r.Year)} — {r.EventName}: {r.FullName} ({r.TeamName})"
            for r in recent_races.itertuples()
        )
 
        recent_driver_form = (
            winners[winners["Year"].isin(last_two)]["FullName"].value_counts()
        )
        recent_driver_str = "\n".join(
            f"  {name}: {count} vitórias" for name, count in recent_driver_form.items()
        )
 
        recent_team_form = (
            winners[winners["Year"].isin(last_two)]["TeamName"].value_counts()
        )
        recent_team_str = "\n".join(
            f"  {name}: {count} vitórias" for name, count in recent_team_form.items()
        )
 
        context = f"""
=== DADOS HISTÓRICOS DE F1 ({all_years[0]}–{all_years[-1]}) ===
 
MAIORES VENCEDORES DE CORRIDAS (todos os tempos):
{driver_wins_str}
 
VITÓRIAS POR EQUIPE (todos os tempos):
{team_wins_str}
 
LÍDERES DE PONTOS POR TEMPORADA:
{champ_str}
 
ÚLTIMAS 10 CORRIDAS:
{recent_str}
 
FORMA RECENTE — PILOTOS ({last_two[0]}–{last_two[1]}):
{recent_driver_str}
 
FORMA RECENTE — EQUIPES ({last_two[0]}–{last_two[1]}):
{recent_team_str}
""".strip()
 
        print(f"[DATA] Contexto pronto: {all_years[0]}–{all_years[-1]}, "
              f"{len(winners)} vitórias indexadas.")
        return context
 
    except Exception:
        print("[DATA] ERRO ao montar o contexto estatístico:")
        traceback.print_exc()
        return "Dados históricos de corridas não disponíveis no momento."