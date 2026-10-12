# Define a decorator for formatting text
def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


class Report:
    # Class variable for storing templates
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template_func):
        cls.templates[name] = template_func

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name, lambda title, content: f"{title}\n{content}")

    # Magic method to call a report instance with a template name
    def __call__(self, template_name):
        template_func = self.get_template(template_name)
        return template_func(self.title, self.content)

    # String representation of the report
    def __str__(self):
        return f"Report Title: {self.title}\nContent: {self.content}"


# Define template functions
def simple_template(title, content):
    return f"--- {title} ---\n{content}"


@bold_text
def fancy_template(title, content):
    return f"*** REPORT: {title} ***\n[Details]: {content}"


# Main function to generate and display reports
def main():
    # Add templates to the Report class
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create a report instance
    report = Report("Quarterly Performance", "Sales increased by 20% in Q3.")

    print("Default String Representation:")
    print(report)
    print("\n" + "="*30 + "\n")

    # Generate reports with different templates using the __call__ magic method
    print("Generating with 'simple' template:")
    print(report("simple"))

    print("\nGenerating with 'fancy' template:")
    print(report("fancy"))


if __name__ == "__main__":
    main()