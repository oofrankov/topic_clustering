import pandas as pd

def preprocess_data(df: pd.DataFrame) -> list[str]:
    """
    Combines 'Заголовок' and 'Опис' columns into a single text per row.

    Args:
        df (pd.DataFrame): A dataframe with 'Опис' and 'Description' columns.

    Returns:
        List[str]: A list of combined and cleaned texts.
    """
    df = df.copy()
    df['Заголовок'] = df['Заголовок'].fillna('').astype(str).str.strip()
    df['Опис'] = df['Опис'].fillna('').astype(str).str.strip()

    combined_texts = (df['Заголовок'] + '. ' + df['Опис']).str.strip()
    return combined_texts.tolist()

def extract_date_days(df: pd.DataFrame) -> list[str]:
    """
    Converts the 'Дата' column to datetime and extracts day-level timestamps.

    Args:
        df (pd.DataFrame): A dataframe with a 'Дата' column in datetime format or as strings.

    Returns:
        List[str]: A list of date strings in 'YYYY-MM-DD' format.
    """
    df = df.copy()
    df['Дата'] = pd.to_datetime(df['Дата'])
    date_days = df['Дата'].dt.to_period("D").astype(str)
    return date_days.tolist()