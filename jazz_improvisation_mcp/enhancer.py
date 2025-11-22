"""
Jazz improvisation prompt enhancer
Transforms user intent into visual sensory parameters using olog specifications
"""

from typing import Dict, List, Optional, Tuple
from olog_loader import JazzImprovisationOlog


class JazzImprovisationEnhancer:
    def __init__(self):
        self.olog = JazzImprovisationOlog()
    
    def enhance_prompt_with_jazz_structure(
        self,
        base_prompt: str,
        harmonic_foundation: str = "Round Midnight",
        solo_phase: str = "development",
        intensity_level: int = 5,
        monk_emphasis: bool = True,
    ) -> Dict:
        """
        Enhance an image prompt with jazz improvisation aesthetic
        
        Args:
            base_prompt: Original image description
            harmonic_foundation: Which Monk composition to anchor (Round Midnight, Evidence, Epistrophy, Ask Me Now)
            solo_phase: Which phase of solo structure (statement, development, resolution)
            intensity_level: 1-10 intensity scale
            monk_emphasis: Whether to emphasize Monk-specific principles
        
        Returns:
            Dictionary with enhanced parameters and synthesis guidelines
        """
        
        # Validate inputs
        if intensity_level < 1 or intensity_level > 10:
            intensity_level = max(1, min(10, intensity_level))
        
        # Get harmonic foundation specification
        hf = self.olog.get_harmonic_foundation(harmonic_foundation)
        if not hf:
            hf = self.olog.get_harmonic_foundation("Round Midnight")
        
        # Get phase specification with correct key format
        phase_key_map = {
            'statement': 'phase_1_statement',
            'development': 'phase_2_development',
            'resolution': 'phase_3_resolution',
        }
        phase_key = phase_key_map.get(solo_phase.lower(), 'phase_2_development')
        phase_spec = self.olog.get_phase_specification(phase_key)
        if not phase_spec:
            phase_spec = self.olog.get_phase_specification('phase_2_development')
        
        # Build intensity profile for this phase
        intensity_profile = self._build_intensity_profile(
            phase=solo_phase,
            intensity_level=intensity_level,
            harmonic_complexity=self._harmonic_complexity_from_foundation(hf),
            monk_emphasis=monk_emphasis
        )
        
        # Get sensory bridge mapping from phase specification
        sensory_intent = {
            'visual_analog': phase_spec.get('visual_analog', 'layering and coherence'),
            'how_it_feels': phase_spec.get('how_it_feels', 'knowledge unfolding'),
        }
        
        # Build enhancement parameters
        enhancement = {
            "harmonic_foundation": hf['name'],
            "harmonic_characteristic": hf['characteristic'],
            "solo_phase": solo_phase,
            "phase_intention": phase_spec.get('narrative_role'),
            "sensory_intention": phase_spec.get('sensory_intention'),
            "intensity_profile": intensity_profile,
            "visual_analog": sensory_intent.get('visual_analog'),
            "how_it_feels": sensory_intent.get('how_it_feels'),
        }
        
        # Add Monk-specific principles if emphasized
        if monk_emphasis:
            monk_visual = self.olog.get_monk_visual_intention()
            phase_key = f"{solo_phase.lower()}_phase_intent"
            if phase_key in monk_visual:
                enhancement['monk_visual_principle'] = monk_visual[phase_key]['visual_equivalent']
                enhancement['monk_sonic_principle'] = monk_visual[phase_key]['sonic']
        
        # Build the enhanced prompt
        enhanced_prompt = self._synthesize_prompt(
            base_prompt=base_prompt,
            enhancement=enhancement,
            solo_phase=solo_phase,
            intensity_level=intensity_level
        )
        
        # Get natural transformations for guidance
        transformations = self.olog.get_natural_transformations()
        
        return {
            "original_prompt": base_prompt,
            "enhanced_prompt": enhanced_prompt,
            "harmonic_foundation": hf['name'],
            "solo_phase": solo_phase,
            "intensity_profile": intensity_profile,
            "sensory_intention": phase_spec.get('sensory_intention'),
            "visual_analog": sensory_intent.get('visual_analog'),
            "how_it_feels": sensory_intent.get('how_it_feels'),
            "monk_principles": enhancement.get('monk_visual_principle'),
            "coherence_note": f"This enhancement maintains the {solo_phase} phase character: {phase_spec.get('narrative_role')}",
            "temporal_note": "This visual should feel like it unfolds through time—constraint establishing, complexity emerging, then clarity resolving",
        }
    
    def _harmonic_complexity_from_foundation(self, hf: Dict) -> int:
        """Map harmonic foundation to complexity score 1-10"""
        complexity_map = {
            "angular_chromatic": 9,
            "bebop_dense": 8,
            "modal_repetition": 4,
            "lyrical_simple": 3,
        }
        return complexity_map.get(hf.get('complexity'), 5)
    
    def _build_intensity_profile(
        self,
        phase: str,
        intensity_level: int,
        harmonic_complexity: int,
        monk_emphasis: bool = True
    ) -> Dict:
        """Build intensity profile respecting natural transformations"""
        
        phase_profile = self.olog.get_phase_intensity_profile(phase)
        
        # Base profile from phase
        if phase.lower() == 'statement':
            note_density = 2 + intensity_level * 0.1
            rhythmic_subdivision = 2 + intensity_level * 0.1
            harmonic_complexity_actual = 1 + intensity_level * 0.1
            rest_space = 7 - intensity_level * 0.2
            
        elif phase.lower() == 'development':
            note_density = 5 + intensity_level * 0.3
            rhythmic_subdivision = 5 + intensity_level * 0.3
            harmonic_complexity_actual = 6 + intensity_level * 0.3
            # Natural transformation: intensity_requires_clarity → high density needs high rest
            rest_space = 4 + intensity_level * 0.4
            
        elif phase.lower() == 'resolution':
            note_density = 3 + intensity_level * 0.2
            rhythmic_subdivision = 3 + intensity_level * 0.2
            harmonic_complexity_actual = 3 + intensity_level * 0.2
            rest_space = 6 - intensity_level * 0.1
            
        else:
            # Default to development
            note_density = 5
            rhythmic_subdivision = 5
            harmonic_complexity_actual = 6
            rest_space = 5
        
        # Apply Monk emphasis
        if monk_emphasis:
            # Monk: silence as structure → increase rest_space
            rest_space = min(10, rest_space + 1.5)
            # Monk: constraint as liberation → can increase harmonic complexity while maintaining clarity
            if harmonic_complexity_actual < harmonic_complexity:
                harmonic_complexity_actual = harmonic_complexity * 0.8
        
        # Clamp to 1-10 range
        profile = {
            "note_density": min(10, max(1, round(note_density))),
            "rhythmic_subdivision": min(10, max(1, round(rhythmic_subdivision))),
            "harmonic_complexity": min(10, max(1, round(harmonic_complexity_actual))),
            "melodic_singularity": 8 if intensity_level < 5 else 6,
            "rest_space": min(10, max(1, round(rest_space))),
            "beat_relationship": 5 + intensity_level * 0.3 if not monk_emphasis else 7 + intensity_level * 0.2,
        }
        
        # Validate against coherence constraints
        valid, msg = self.olog.validate_intensity_profile(profile)
        profile["coherence_valid"] = valid
        profile["coherence_note"] = msg
        
        return profile
    
    def _synthesize_prompt(
        self,
        base_prompt: str,
        enhancement: Dict,
        solo_phase: str,
        intensity_level: int
    ) -> str:
        """Synthesize enhanced prompt from base prompt and enhancement parameters"""
        
        phase_keywords = {
            'statement': [
                "sharp focus, established baseline",
                "clarity entering, defined edges",
                "foundational structure, reference point",
                f"harmonic foundation of {enhancement['harmonic_foundation']} clarity"
            ],
            'development': [
                "layering, complexity emerging from pattern",
                "density increasing yet coherent",
                "revealed structure within apparent chaos",
                "intense exploration within constraint",
                "patterns visible through texture",
                f"exploring {enhancement['harmonic_characteristic']}",
                "mastery accumulating through variation"
            ],
            'resolution': [
                "clarity restored, pattern now visible",
                "complexity synthesized into unified whole",
                "earned knowledge integrated",
                "precision and confidence",
                f"returning to {enhancement['harmonic_foundation']} with understanding"
            ]
        }
        
        # Get phase-specific keywords
        keywords = phase_keywords.get(solo_phase.lower(), phase_keywords['development'])
        
        # Build intensity descriptor
        intensity_desc = {
            1: "minimal, sparse",
            2: "restrained, foundational",
            3: "subtle, emergent",
            4: "modest, controlled",
            5: "balanced, moderate",
            6: "building, intensifying",
            7: "complex, layered",
            8: "dense, intricate",
            9: "extreme, maximum variation",
            10: "total saturation, complete exploration"
        }
        
        intensity_word = intensity_desc.get(intensity_level, "moderate")
        
        # Synthesize prompt
        enhanced = (
            f"{base_prompt}, "
            f"with the sensory character of a jazz solo in the {solo_phase} phase: "
            f"{enhancement['how_it_feels']}. "
            f"Visual treatment: {', '.join(keywords[:2])}. "
            f"Intensity profile: {intensity_word}. "
            f"The image should feel like it's {enhancement['sensory_intention']}. "
            f"Visual analog: {enhancement['visual_analog']}. "
        )
        
        if enhancement.get('monk_visual_principle'):
            enhanced += f"Monk principle: {enhancement['monk_visual_principle']} "
        
        return enhanced
    
    def get_all_harmonic_foundations(self) -> List[Dict]:
        """Get all available harmonic foundations"""
        return self.olog.get_harmonic_foundations()
    
    def get_all_phases(self) -> List[str]:
        """Get all available solo phases"""
        return ['statement', 'development', 'resolution']
    
    def compare_phases_intensity(self, harmonic_foundation: str = "Round Midnight") -> Dict:
        """Compare intensity profiles across all three phases"""
        profiles = {}
        for phase in self.get_all_phases():
            profiles[phase] = self._build_intensity_profile(
                phase=phase,
                intensity_level=5,
                harmonic_complexity=self._harmonic_complexity_from_foundation(
                    self.olog.get_harmonic_foundation(harmonic_foundation)
                )
            )
        return profiles
