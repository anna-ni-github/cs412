#voter_analytics/models.py
#author: Anna Ni (annani@bu.edu)
#description: Django model representing registered voters in Newton, MA

from django.db import models

class Voter(models.Model):
    """Model representing a registered voter in Newton, MA."""
    
    # Personal Information
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    
    # Address Information
    street_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    
    # Voter Information
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    party_affiliation = models.CharField(max_length=2)
    precinct_number = models.CharField(max_length=10)
    
    # Election Participation (Boolean fields for each election)
    v20state = models.BooleanField(default=False)
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)
    
    # Voter Score
    voter_score = models.IntegerField(default=0)
    
    def __str__(self):
        """String representation of a Voter."""
        return f"{self.first_name} {self.last_name} - {self.street_number} {self.street_name}, Precinct {self.precinct_number}"
    
    class Meta:
        ordering = ['last_name', 'first_name']


def load_data():
    """
    Function to load data records from CSV file into Django model instances.
    """
    
    # Delete existing records to avoid duplicates
    Voter.objects.all().delete()
    
    filename = '/Users/annani/Downloads/newton_voters.csv'
    f = open(filename)
    headers = f.readline()  # discard headers
    
    print("Loading data...")
    
    for line in f:
        
        try:
            fields = line.split(',')
            
            # Create a new instance of Voter object with this record from CSV
            voter = Voter(
                last_name=fields[1],
                first_name=fields[2],
                street_number=fields[3],
                street_name=fields[4],
                apartment_number=fields[5] if fields[5] else None,
                zip_code=fields[6],
                date_of_birth=fields[7],
                date_of_registration=fields[8],
                party_affiliation=fields[9].strip(),
                precinct_number=fields[10],
                v20state=(fields[11].strip().upper() == 'TRUE'),
                v21town=(fields[12].strip().upper() == 'TRUE'),
                v21primary=(fields[13].strip().upper() == 'TRUE'),
                v22general=(fields[14].strip().upper() == 'TRUE'),
                v23town=(fields[15].strip().upper() == 'TRUE'),
                voter_score=int(fields[16]),
            )
            
            voter.save()  # commit to database
            print(f'Created voter: {voter}')
            
        except Exception as e:
            print(f"Skipped: {fields}")
            print(f"Exception: {e}")
    
    print(f'Done. Created {len(Voter.objects.all())} Voters.')