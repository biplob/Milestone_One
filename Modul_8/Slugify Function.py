def slugify(text):
    slug = text.strip().lower().replace(' ','-')
    while '--' in slug:
        slug = slug.replace('--','-')
    return slug

title = input('Enter the main keyword: ')
slugin = slugify(title)
print(slugin)