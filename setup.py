from setuptools import setup, find_packages

setup(
    name = "z3c.baseregistry",
    version = "0.1dev",
    author = "Zope Contributors",
    author_email = "zope3-dev@zope.org",
    description = "Manage IComponents instances using Python code and ZCML.",
    license = "ZPL 2.1",
    keywords = "zope3 baseregistry",
    url = 'http://svn.zope.org/z3c.baseregistry',
    classifiers = [
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: Zope Public License",
        "Framework :: Zope :: UI"],
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['z3c'],
    zip_safe = False,
    extras_require = dict(test=['zope.app.testing',
                                'zope.testing',
                               ]),
    install_requires = ['setuptools',
                        'zope.app.component',
                        'zope.app.i18n',
                        'zope.app.pagetemplate',
                        'zope.component',
                        'zope.configuration',
                        'zope.formlib',
                        'zope.i18nmessageid',
                        'zope.interface',
                        'zope.schema',
                        ],
)
