def extract_first_sentence(text: str) -> str:
    """
    Args:
        text (str): Input text.

    Returns:
        str: The first sentence extracted from the text.
    """
    sentence = text.split(".")[0].strip()
    return sentence if sentence else text.strip()

def get_representative_doc(topic_model, topic_id: int) -> str:
    """
    Args:
        topic_model: BERTopic model instance.
        topic_id (int): ID of the topic.

    Returns:
        str: Representative document for the given topic.
    """
    topic_info = topic_model.get_topic_info()
    rep_doc = topic_info[topic_info["Topic"] == topic_id]["Representative_Docs"].values[0][0]
    return rep_doc

def generate_topic_labels(topic_model, topic_ids: list[int]) -> dict:
    """
    Args:
        topic_model: BERTopic model instance.
        topic_ids (list[int]): List of topic IDs.

    Returns:
        dict[int, str]: Mapping from topic IDs to their generated labels.
    """
    labels = {}
    for topic_id in topic_ids:
        rep_doc = get_representative_doc(topic_model, topic_id)
        label = extract_first_sentence(rep_doc)
        labels[topic_id] = label
    return labels