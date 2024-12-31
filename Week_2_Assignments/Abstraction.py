#High-Level Function (Abstract)

def prepare_meal():
    gather_ingredients()
    cook_food()
    serve_meal()


#Mid-Level Functions (More Specific)

def gather_ingredients():
    get_vegetables()
    get_spices()
    get_protein()

def cook_food():
    chop_ingredients()
    heat_pan()
    combine_ingredients()
    cook_on_stove()

def serve_meal():
    plate_food()
    garnish_food()
    set_table()

#Low-Level Functions (Concrete Implementation)

def get_vegetables():
    print("Buying carrots, onions, and tomatoes.")

def get_spices():
    print("Getting salt, pepper, and turmeric.")

def get_protein():
    print("Selecting chicken and tofu.")

def chop_ingredients():
    print("Chopping vegetables and protein into small pieces.")

def heat_pan():
    print("Heating the pan with a little oil.")

def combine_ingredients():
    print("Adding vegetables, protein, and spices into the pan.")

def cook_on_stove():
    print("Cooking the mixture for 15 minutes on medium heat.")
