"""
Jazz improvisation olog loader
Reads categorical structure and intentionality reasoning from YAML
"""

import yaml
import os
from pathlib import Path


class JazzImprovisationOlog:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.categorical_structure = None
        self.intentionality_reasoning = None
        self._load_ologs()
    
    def _load_ologs(self):
        """Load both olog YAML files"""
        cat_path = self.base_path / "categorical_structure.yaml"
        intent_path = self.base_path / "intentionality_reasoning.yaml"
        
        with open(cat_path, 'r') as f:
            self.categorical_structure = yaml.safe_load(f)
        
        with open(intent_path, 'r') as f:
            self.intentionality_reasoning = yaml.safe_load(f)
    
    def get_harmonic_foundations(self):
        """Get all available harmonic foundations (chord progressions)"""
        return self.categorical_structure['types']['harmonic_foundation']['instances']
    
    def get_harmonic_foundation(self, name):
        """Get specific harmonic foundation by name"""
        for hf in self.get_harmonic_foundations():
            if hf['name'] == name:
                return hf
        return None
    
    def get_intensity_dimensions(self):
        """Get intensity arc dimensions"""
        return self.categorical_structure['types']['intensity_arc']['dimensions']
    
    def get_phrasing_clarity_dimensions(self):
        """Get phrasing clarity dimensions"""
        return self.categorical_structure['types']['phrasing_clarity']['dimensions']
    
    def get_temporal_pacing_dimensions(self):
        """Get temporal pacing dimensions"""
        return self.categorical_structure['types']['temporal_pacing']['dimensions']
    
    def get_morphisms(self):
        """Get all morphism definitions"""
        return self.categorical_structure['morphisms']
    
    def get_natural_transformations(self):
        """Get natural transformation rules"""
        return self.categorical_structure['natural_transformations']
    
    def get_monk_principles(self):
        """Get Monk-specific anchor principles"""
        return self.categorical_structure['monk_anchor_principles']
    
    def get_phase_specification(self, phase_name):
        """Get phase specification from intentionality reasoning"""
        # Handle different phase_name formats
        if phase_name.startswith('phase_'):
            return self.intentionality_reasoning.get(phase_name)
        
        # Map simple names to full keys
        phase_key_map = {
            'statement': 'phase_1_statement',
            'development': 'phase_2_development',
            'resolution': 'phase_3_resolution',
        }
        phase_key = phase_key_map.get(phase_name.lower(), f"phase_{phase_name.lower()}")
        return self.intentionality_reasoning.get(phase_key)
    
    def get_all_phases(self):
        """Get all three phases with their intentionality"""
        return {
            'statement': self.intentionality_reasoning.get('phase_1_statement'),
            'development': self.intentionality_reasoning.get('phase_2_development'),
            'resolution': self.intentionality_reasoning.get('phase_3_resolution'),
        }
    
    def get_sensory_bridge(self):
        """Get visual-sensory bridge mappings"""
        return self.intentionality_reasoning.get('sensory_bridge')
    
    def get_monk_visual_intention(self):
        """Get Monk-specific visual-sensory intentions"""
        return self.intentionality_reasoning.get('monk_visual_sensory_intention')
    
    def get_coherence_constraints(self):
        """Get coherence constraint definitions"""
        return self.categorical_structure['coherence_constraints']
    
    def validate_intensity_profile(self, intensity_dict):
        """Validate that intensity profile respects natural transformations"""
        constraints = self.get_natural_transformations()
        
        # Constraint: intensity_requires_clarity
        # When intensity increases, rest_space must increase
        if intensity_dict.get('note_density', 5) > 6:
            if intensity_dict.get('rest_space', 5) < 6:
                return False, "High note density requires high rest space for legibility"
        
        # Constraint: harmonic_complexity_drives_phrasing_response
        if intensity_dict.get('harmonic_complexity', 5) > 7:
            if intensity_dict.get('melodic_singularity', 5) < 6:
                return False, "High harmonic complexity requires high melodic singularity"
        
        # Constraint: temporal_displacement_needs_harmonic_anchor
        # Behind-the-beat (beat_relationship > 7) needs either explicit harmonic_clarity
        # or we can use harmonic_complexity as a proxy
        if intensity_dict.get('beat_relationship', 5) > 7:
            # If behind beat, harmonic complexity should be reasonable (not too low)
            if intensity_dict.get('harmonic_complexity', 5) < 4:
                return False, "Behind-the-beat playing needs harmonic complexity for anchor"
        
        return True, "Intensity profile is coherent"
    
    def get_phase_intensity_profile(self, phase_name):
        """Get the recommended intensity profile for a specific phase"""
        morphism = self.categorical_structure['morphisms']['statement_development_resolution']
        
        phase_key = phase_name.lower()
        if phase_key in morphism:
            return morphism[phase_key].get('intensity_profile')
        return None
