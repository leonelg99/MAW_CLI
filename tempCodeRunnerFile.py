 if img.width > max_width or img.height > max_height:
        img.thumbnail((max_width, max_height))