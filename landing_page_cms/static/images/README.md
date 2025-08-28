# 🐱 Cat Images for Kitty Corner

## How to Add Real Cat Photos

1. **Upload your cat photos** to this folder
2. **Recommended formats**: JPG, PNG, WebP
3. **Recommended sizes**: 
   - Cat photos: 400x400px or larger
   - Avatar photos: 200x200px or larger
4. **File naming**: Use descriptive names like `luna-black-cat.jpg`, `whiskers-orange-tabby.jpg`

## Current Placeholder Images

The landing page currently uses emoji placeholders:
- 🐈‍⬛ Luna (black cat)
- 🐈 Whiskers (orange tabby)  
- 🐱 Mittens (playful cat)

## To Replace with Real Images

1. Upload your photos to this folder
2. Edit the template file: `home/templates/home/kitty_landing_page.html`
3. Replace the emoji placeholders with `<img>` tags
4. Run `python manage.py collectstatic` to update static files

## Example Image Replacement

**Before (emoji):**
```html
<span>🐈‍⬛</span>
```

**After (real image):**
```html
<img src="{% static 'images/luna-black-cat.jpg' %}" alt="Luna the black cat">
```

## Free Cat Image Resources

- [Unsplash](https://unsplash.com/s/photos/cat) - Free high-quality photos
- [Pexels](https://www.pexels.com/search/cat/) - Free stock photos
- [Pixabay](https://pixabay.com/images/search/cat/) - Free images

Remember to respect image licenses and attribution requirements!
