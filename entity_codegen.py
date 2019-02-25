"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    #Construye un modelo de fibonacci desde el archivo fibonacci.ent 
    fibonacci_model = entity_mm.model_from_file(join(this_folder, 'fibonacci.ent'))

    def is_entity(n):
        #Comprueba si es una entidad
        if n.type in fibonacci_model.entities:
            return True
        else:
            return False

    def c_type(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['c_type'] = c_type

    # Load template
    template = jinja_env.get_template('clase.template')

    for entity in fibonacci_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%s.cpp" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    
if __name__ == "__main__":
    main()
