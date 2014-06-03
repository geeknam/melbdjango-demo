#
# MelbDjango - Pipeline Example
# Loose coupling
#

PIPELINE = (
    'validation.contains_dot',
    'validation.contains_at',
    'mutators.lowercase_domain',
    'mutators.lowercase_name',
)


class EmailValidator(object):

    def __init__(self, email):

        self._pipelines = []
        self.load_pipelines()
        self.email = email

        for func in self._pipelines:
            res = func(self.email)
            if res:
                self.email = res

    def get_email(self):
        return self.email

    def load_pipelines(self):
        for line in PIPELINE:
            mod_name, func_name = line.split('.')
            mod = __import__(mod_name)
            func = getattr(mod, func_name)
            self._pipelines.append(func)


email = EmailValidator('Test@UPPER.COM').get_email()
print email