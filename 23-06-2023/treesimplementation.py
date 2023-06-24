#dictionary(forest of 3 trees)
Families={ 'charley':{'sam':{'boxy','rosy'},'nila':{'pepsi'}},'devi':{'tommy':{'tony'},'timmy':{'hamster'},'tammy':{'hamster'}},'carlos':{'diego':'cat','ferret':'fox'}}
for Parent, Children in Families.items():
    print(f"{Parent} hs {len(Children)} kid(s):")
    print(f"{', and '.join([str(Child) for Child in [*Children]])}")