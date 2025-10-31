#voter_analytics/views.py
#author: Anna Ni (annani@bu.edu)
# Views for displaying voter records and graphs

from django.views.generic import ListView
from .models import Voter
import plotly
import plotly.graph_objs as go
from collections import Counter


class VoterListView(ListView):
    '''View to display voter records'''
    
    template_name = 'voter_analytics/voter_list.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100
    
    def get_queryset(self):
        '''Filter the queryset based on GET parameters'''
        
        # Start with entire queryset
        qs = super().get_queryset()
        
        # Filter by party affiliation
        if 'party_affiliation' in self.request.GET:
            party = self.request.GET['party_affiliation']
            if party:
                qs = qs.filter(party_affiliation=party)
        
        # Filter by minimum birth year
        if 'min_birth_year' in self.request.GET:
            min_year = self.request.GET['min_birth_year']
            if min_year:
                qs = qs.filter(date_of_birth__year__gte=min_year)
        
        # Filter by maximum birth year
        if 'max_birth_year' in self.request.GET:
            max_year = self.request.GET['max_birth_year']
            if max_year:
                qs = qs.filter(date_of_birth__year__lte=max_year)
        
        # Filter by voter score
        if 'voter_score' in self.request.GET:
            score = self.request.GET['voter_score']
            if score:
                qs = qs.filter(voter_score=score)
        
        # Filter by specific elections (checkboxes)
        if 'v20state' in self.request.GET:
            qs = qs.filter(v20state=True)
        
        if 'v21town' in self.request.GET:
            qs = qs.filter(v21town=True)
        
        if 'v21primary' in self.request.GET:
            qs = qs.filter(v21primary=True)
        
        if 'v22general' in self.request.GET:
            qs = qs.filter(v22general=True)
        
        if 'v23town' in self.request.GET:
            qs = qs.filter(v23town=True)
        
        return qs
    
    def get_context_data(self, **kwargs):
        '''Add additional context data for the template'''
        context = super().get_context_data(**kwargs)
        
        # Get unique party affiliations for dropdown
        context['party_affiliations'] = Voter.objects.values_list('party_affiliation', flat=True).distinct().order_by('party_affiliation')
        
        # Get year range for birth year dropdowns
        context['birth_years'] = range(1920, 2010)
        
        # Get voter scores for dropdown
        context['voter_scores'] = range(0, 6)
        
        return context


class GraphsView(ListView):
    '''View to display graphs of voter data'''
    
    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'voters'
    
    def get_queryset(self):
        '''Filter the queryset based on GET parameters (same as VoterListView)'''
        
        # Start with entire queryset
        qs = super().get_queryset()
        
        # Filter by party affiliation
        if 'party_affiliation' in self.request.GET:
            party = self.request.GET['party_affiliation']
            if party:
                qs = qs.filter(party_affiliation=party)
        
        # Filter by minimum birth year
        if 'min_birth_year' in self.request.GET:
            min_year = self.request.GET['min_birth_year']
            if min_year:
                qs = qs.filter(date_of_birth__year__gte=min_year)
        
        # Filter by maximum birth year
        if 'max_birth_year' in self.request.GET:
            max_year = self.request.GET['max_birth_year']
            if max_year:
                qs = qs.filter(date_of_birth__year__lte=max_year)
        
        # Filter by voter score
        if 'voter_score' in self.request.GET:
            score = self.request.GET['voter_score']
            if score:
                qs = qs.filter(voter_score=score)
        
        # Filter by specific elections (checkboxes)
        if 'v20state' in self.request.GET:
            qs = qs.filter(v20state=True)
        
        if 'v21town' in self.request.GET:
            qs = qs.filter(v21town=True)
        
        if 'v21primary' in self.request.GET:
            qs = qs.filter(v21primary=True)
        
        if 'v22general' in self.request.GET:
            qs = qs.filter(v22general=True)
        
        if 'v23town' in self.request.GET:
            qs = qs.filter(v23town=True)
        
        return qs
    
    def get_context_data(self, **kwargs):
        '''Add graph data to context'''
        context = super().get_context_data(**kwargs)
        
        # Get the filtered queryset
        voters = self.get_queryset()
        
        # Graph 1: Distribution by birth year
        birth_years = [voter.date_of_birth.year for voter in voters]
        year_counts = Counter(birth_years)
        
        # Sort by year
        sorted_years = sorted(year_counts.items())
        years = [year for year, count in sorted_years]
        counts = [count for year, count in sorted_years]
        
        fig_birth_year = go.Figure(data=[
            go.Bar(x=years, y=counts)
        ])
        fig_birth_year.update_layout(
            title='Distribution of Voters by Year of Birth',
            xaxis_title='Year of Birth',
            yaxis_title='Number of Voters'
        )
        context['birth_year_graph'] = plotly.offline.plot(
            fig_birth_year, 
            auto_open=False, 
            output_type='div'
        )
        
        # Graph 2: Distribution by party affiliation (pie chart)
        party_counts = Counter([voter.party_affiliation for voter in voters])
        
        fig_party = go.Figure(data=[
            go.Pie(labels=list(party_counts.keys()), 
                   values=list(party_counts.values()))
        ])
        fig_party.update_layout(
            title='Distribution of Voters by Party Affiliation'
        )
        context['party_graph'] = plotly.offline.plot(
            fig_party, 
            auto_open=False, 
            output_type='div'
        )
        
        # Graph 3: Distribution by election participation
        elections = {
            'v20state': '2020 State',
            'v21town': '2021 Town',
            'v21primary': '2021 Primary',
            'v22general': '2022 General',
            'v23town': '2023 Town'
        }
        
        election_counts = {}
        for field, label in elections.items():
            count = voters.filter(**{field: True}).count()
            election_counts[label] = count
        
        fig_elections = go.Figure(data=[
            go.Bar(x=list(election_counts.keys()), 
                   y=list(election_counts.values()))
        ])
        fig_elections.update_layout(
            title='Distribution of Voters by Election Participation',
            xaxis_title='Election',
            yaxis_title='Number of Voters Who Participated'
        )
        context['elections_graph'] = plotly.offline.plot(
            fig_elections, 
            auto_open=False, 
            output_type='div'
        )
        
        # Add filter options for the form
        context['party_affiliations'] = Voter.objects.values_list('party_affiliation', flat=True).distinct().order_by('party_affiliation')
        context['birth_years'] = range(1920, 2010)
        context['voter_scores'] = range(0, 6)
        
        return context