from bhs_book import BhsBook


def main():
    new_book = BhsBook(
        identifier="backhandstories.com-one",
        title="Backhand Stories: Anthology One",
        author="Martin Bell",
    )

    replacement_rules = {
        r"<\!\-*\w*\-*\>": "",
        r"--": " — ",
        r"(?:\\+\w)+": "</p><p>",
        r"\\": "",
    }
    story_ids = [27, 45]
    connection = new_book.connect_to_db()
    paths = []
    for story_id in story_ids:
        data = new_book.get_story(story_id, connection)
        cleaned_story = new_book.clean_story(data[1], replacement_rules)
        paths.append(
            new_book.write_html(data[0], cleaned_story, story_ids.index(story_id))
        )
    connection.close()
    new_book.collate_chapters(paths)
    return


if __name__ == "__main__":
    main()
