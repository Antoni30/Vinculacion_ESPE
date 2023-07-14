from models.Person import Person
from models.Internal import Internal

if __name__ == "__main__":

    user=Person("Diego Alexnader","Paez Zapata","1750343210","dapaez3@espe.edu.ec")
    user.toString()
    user.greet()
    user_internal = Internal("Jimena","Tutillo","1750463278","jstutillo@espe.edu.ec","L03532","student","matriz","administrativa")
    user_internal.greet_internal()
