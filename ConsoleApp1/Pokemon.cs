using System;

class Pokemon {
    public static void Main (string[] args)
    {
        Pokemon pikachu = new Pokemon("Pikachu", "Sparky", "Electric", "Ground");
    }
}

class Pokemon
{
    public string species;
    public string name;
    public string type;
    public string weakness;

    public Pokemon(string species, string name, string type, string weakness)
    {
        this.species = species;
        this.name = name;
        this.type = type;
        this.weakness = weakness;
    }

    public string getName()
    {
        return name;
    }
    public string getType()
    {
        return type;
    }
    public string getSpecies()
    {
        return species;
    }
    public string getWeakness()
    {
        return weakness;
    }
    
}