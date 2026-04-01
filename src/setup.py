from setuptools import setup
import setup_translate

pkg = 'Extensions.DLNABrowser'
setup(name='enigma2-plugin-extensions-dlnabrowser',
       version='3.0',
       description='this is dlna/upnp browser using djmount',
       package_dir={pkg: 'DLNABrowser'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'icons/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
