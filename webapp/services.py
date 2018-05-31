class MetaBag:
    def __init__(self, title=None, description=None, url=None, images=[]):
        self.title = title
        self.description = description
        self.url = url
        self.images = images
        self.type = 'website'


class BreadcrumbBag:
    class Breadcrumb:
        def __init__(self, name, url, css_classes):
            self.name = name
            self.url = url
            self.css_classes = css_classes

    def __init__(self, items=[]):
        self.items = []

        for item in items:
            self.add(*item)

    def add(self, name, url=None, css_classes=''):
        self.items.append(self.Breadcrumb(name, url, css_classes))
