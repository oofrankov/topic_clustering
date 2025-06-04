import os

def save_result_topics(topic_model, output_path: str):
    """
    Saves the most popular topics (excluding the outlier topic -1) to a CSV file.

    Args:
        topic_model: A fitted BERTopic model.
        output_path (str): File path to save the CSV.
    """

    # Ensure the parent directory exists
    parent_dir = os.path.dirname(output_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)

    topic_info = topic_model.get_topic_info()
    filtered = topic_info[topic_info.Topic != -1]
    filtered[["Count", "CustomName"]].to_csv(output_path, index=False)