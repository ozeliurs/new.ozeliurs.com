import markdown


def render_md(path: str) -> (dict, str):
    """Render a markdown file to HTML."""

    with open(f"content/{path.strip('/')}", "r") as f:
        content = f.read()

    if content.startswith("---"):
        metadata = content.split("---", 2)[1]
        content = content.split("---", 2)[2]

    metadata = {k.strip(): v.strip() for k, v in [line.split(":") for line in metadata.splitlines() if line]}

    content = markdown.markdown(content, extensions=["extra"])

    return metadata, content
