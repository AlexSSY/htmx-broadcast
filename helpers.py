def get_id(obj, prefix=None):
    """
    returns model's unique DOM id
    """
    model = obj.__class__.__name__.lower()
    identifier = getattr(obj, 'id', None) or getattr(obj, 'pk', None)
    base = f"{model}_{identifier}" if identifier is not None else f"new_{model}"
    return f"{prefix}_{base}" if prefix else base
