from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import (
    CharBlock, TextBlock, RichTextBlock,
    StructBlock, ListBlock, URLBlock, ChoiceBlock
)
from wagtail.images.blocks import ImageChooserBlock as WagtailImageChooserBlock


class HeroSectionBlock(StructBlock):
    """Main banner with title, subtitle and button"""
    title = CharBlock(max_length=100, help_text="Main title")
    subtitle = TextBlock(help_text="Subtitle under the main title")
    button_text = CharBlock(max_length=50, default="Learn More", help_text="Button text")
    button_url = URLBlock(required=False, help_text="Button link")
    background_image = WagtailImageChooserBlock(required=False, help_text="Background image")

    class Meta:
        template = "home/blocks/hero_section.html"
        icon = "image"
        label = "Hero Section"


class FeatureBlock(StructBlock):
    """Block with advantage/feature"""
    title = CharBlock(max_length=100, help_text="Feature title")
    description = TextBlock(help_text="Feature description")
    icon = CharBlock(max_length=50, help_text="Icon name (e.g.: star, heart, rocket)")
    image = WagtailImageChooserBlock(required=False, help_text="Image for the feature")

    class Meta:
        template = "home/blocks/feature.html"
        icon = "pick"
        label = "Feature"


class TestimonialBlock(StructBlock):
    """Block with customer review"""
    name = CharBlock(max_length=100, help_text="Customer name")
    position = CharBlock(max_length=100, help_text="Position or company")
    text = TextBlock(help_text="Review text")
    avatar = WagtailImageChooserBlock(required=False, help_text="Customer photo")

    class Meta:
        template = "home/blocks/testimonial.html"
        icon = "user"
        label = "Testimonial"


class ContactFormBlock(StructBlock):
    """Block with contact form"""
    title = CharBlock(max_length=100, default="Contact Us", help_text="Form title")
    description = TextBlock(help_text="Form description", required=False)
    submit_button_text = CharBlock(max_length=50, default="Send", help_text="Submit button text")

    class Meta:
        template = "home/blocks/contact_form.html"
        icon = "mail"
        label = "Contact Form"


class HomePage(Page):
    """Home page with StreamField for flexible content"""
    
    # Main page fields
    intro = RichTextField(blank=True, help_text="Brief company introduction")
    
    # StreamField for flexible content
    content = StreamField([
        ('hero_section', HeroSectionBlock()),
        ('rich_text', RichTextBlock(icon="doc-full", label="Rich Text")),
        ('image', WagtailImageChooserBlock(icon="image", label="Image")),
        ('features', ListBlock(FeatureBlock(), icon="list-ul", label="Features List")),
        ('testimonials', ListBlock(TestimonialBlock(), icon="user", label="Testimonials List")),
        ('contact_form', ContactFormBlock()),
    ], blank=True, use_json_field=True, help_text="Add various content blocks")

    # SEO and meta information
    meta_description = models.CharField(max_length=160, blank=True, help_text="Description for search engines")
    keywords = models.CharField(max_length=500, blank=True, help_text="Keywords separated by commas")

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('content'),
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('meta_description'),
            FieldPanel('keywords'),
        ], heading="SEO"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
