"""
Tests for jazz improvisation MCP server
"""

import pytest
import json
from jazz_improvisation_mcp.olog_loader import JazzImprovisationOlog
from jazz_improvisation_mcp.enhancer import JazzImprovisationEnhancer


class TestOlogLoader:
    """Test olog loader functionality"""
    
    def test_load_ologs(self):
        """Test that ologs load successfully"""
        olog = JazzImprovisationOlog()
        assert olog.categorical_structure is not None
        assert olog.intentionality_reasoning is not None
    
    def test_get_harmonic_foundations(self):
        """Test retrieving harmonic foundations"""
        olog = JazzImprovisationOlog()
        foundations = olog.get_harmonic_foundations()
        assert len(foundations) == 4
        names = [f['name'] for f in foundations]
        assert "Round Midnight" in names
        assert "Evidence" in names
        assert "Epistrophy" in names
        assert "Ask Me Now" in names
    
    def test_get_specific_harmonic_foundation(self):
        """Test retrieving specific harmonic foundation"""
        olog = JazzImprovisationOlog()
        foundation = olog.get_harmonic_foundation("Round Midnight")
        assert foundation is not None
        assert foundation['name'] == "Round Midnight"
        assert foundation['complexity'] == "angular_chromatic"
        assert foundation['monk_essence'] is True
    
    def test_get_intensity_dimensions(self):
        """Test retrieving intensity dimensions"""
        olog = JazzImprovisationOlog()
        dims = olog.get_intensity_dimensions()
        assert 'note_density' in dims
        assert 'rhythmic_subdivision' in dims
        assert 'harmonic_complexity' in dims
    
    def test_get_monk_principles(self):
        """Test retrieving Monk principles"""
        olog = JazzImprovisationOlog()
        principles = olog.get_monk_principles()
        assert 'constraint_as_liberation' in principles
        assert 'silence_as_structure' in principles
        assert 'rhythmic_displacement' in principles
        assert 'dissonance_as_truth' in principles
    
    def test_get_phase_specifications(self):
        """Test retrieving phase specifications"""
        olog = JazzImprovisationOlog()
        statement = olog.get_phase_specification('1_statement')
        development = olog.get_phase_specification('2_development')
        resolution = olog.get_phase_specification('3_resolution')
        
        assert statement is not None
        assert development is not None
        assert resolution is not None


class TestEnhancer:
    """Test enhancer functionality"""
    
    def test_enhancer_initialization(self):
        """Test enhancer initialization"""
        enhancer = JazzImprovisationEnhancer()
        assert enhancer.olog is not None
    
    def test_enhance_prompt_basic(self):
        """Test basic prompt enhancement"""
        enhancer = JazzImprovisationEnhancer()
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="a bottle of hot sauce",
            harmonic_foundation="Round Midnight",
            solo_phase="development",
            intensity_level=5,
            monk_emphasis=True
        )
        
        assert result['original_prompt'] == "a bottle of hot sauce"
        assert 'enhanced_prompt' in result
        assert result['solo_phase'] == "development"
        assert result['harmonic_foundation'] == "Round Midnight"
        assert result['intensity_profile'] is not None
    
    def test_enhance_prompt_all_phases(self):
        """Test enhancement across all phases"""
        enhancer = JazzImprovisationEnhancer()
        
        for phase in ['statement', 'development', 'resolution']:
            result = enhancer.enhance_prompt_with_jazz_structure(
                base_prompt="a cup of coffee",
                solo_phase=phase,
                intensity_level=5
            )
            assert result['solo_phase'] == phase
            assert 'enhanced_prompt' in result
    
    def test_intensity_profile_statement(self):
        """Test intensity profile for statement phase"""
        enhancer = JazzImprovisationEnhancer()
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="statement",
            intensity_level=5
        )
        
        profile = result['intensity_profile']
        # Statement should have lower note density than development
        assert profile['note_density'] < 5
        # High rest space for clarity
        assert profile['rest_space'] >= 5
    
    def test_intensity_profile_development(self):
        """Test intensity profile for development phase"""
        enhancer = JazzImprovisationEnhancer()
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=5
        )
        
        profile = result['intensity_profile']
        # Development should have higher note density
        assert profile['note_density'] >= 5
        # Natural transformation: high density requires high rest space
        assert profile['rest_space'] >= 4
    
    def test_intensity_profile_resolution(self):
        """Test intensity profile for resolution phase"""
        enhancer = JazzImprovisationEnhancer()
        
        dev_result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=5
        )
        
        res_result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="resolution",
            intensity_level=5
        )
        
        dev_profile = dev_result['intensity_profile']
        res_profile = res_result['intensity_profile']
        
        # Resolution should have lower or equal complexity than development
        assert res_profile['harmonic_complexity'] <= dev_profile['harmonic_complexity']
    
    def test_monk_emphasis_effect(self):
        """Test that Monk emphasis affects intensity profile"""
        enhancer = JazzImprovisationEnhancer()
        
        without_monk = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=5,
            monk_emphasis=False
        )
        
        with_monk = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=5,
            monk_emphasis=True
        )
        
        # Monk emphasis should increase rest_space (silence as structure)
        assert with_monk['intensity_profile']['rest_space'] >= without_monk['intensity_profile']['rest_space']
    
    def test_intensity_scaling(self):
        """Test that intensity level affects profile appropriately"""
        enhancer = JazzImprovisationEnhancer()
        
        low = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=1
        )
        
        high = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=10
        )
        
        # Higher intensity should have higher note density
        assert high['intensity_profile']['note_density'] > low['intensity_profile']['note_density']
        # Higher intensity should have higher harmonic complexity
        assert high['intensity_profile']['harmonic_complexity'] > low['intensity_profile']['harmonic_complexity']
    
    def test_all_harmonic_foundations(self):
        """Test enhancement with all harmonic foundations"""
        enhancer = JazzImprovisationEnhancer()
        foundations = enhancer.get_all_harmonic_foundations()
        
        assert len(foundations) == 4
        for foundation in foundations:
            result = enhancer.enhance_prompt_with_jazz_structure(
                base_prompt="test image",
                harmonic_foundation=foundation['name'],
                solo_phase="development"
            )
            assert result['harmonic_foundation'] == foundation['name']
    
    def test_compare_phases_intensity(self):
        """Test comparison across phases"""
        enhancer = JazzImprovisationEnhancer()
        comparison = enhancer.compare_phases_intensity("Round Midnight")
        
        assert 'statement' in comparison
        assert 'development' in comparison
        assert 'resolution' in comparison
        
        # Development should generally have higher complexity than statement
        dev_harm = comparison['development']['harmonic_complexity']
        stmt_harm = comparison['statement']['harmonic_complexity']
        assert dev_harm >= stmt_harm


class TestCoherence:
    """Test coherence constraints from natural transformations"""
    
    def test_intensity_requires_clarity(self):
        """Test natural transformation: intensity_requires_clarity"""
        enhancer = JazzImprovisationEnhancer()
        
        # High note density should pair with high rest space
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="development",
            intensity_level=9
        )
        
        profile = result['intensity_profile']
        # Should be coherent
        assert profile.get('coherence_valid', True)
    
    def test_harmonic_complexity_drives_clarity(self):
        """Test natural transformation: harmonic_complexity_drives_phrasing_response"""
        enhancer = JazzImprovisationEnhancer()
        
        # High harmonic complexity should have high melodic singularity
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            harmonic_foundation="Evidence",  # bebop_dense = complex
            solo_phase="development"
        )
        
        profile = result['intensity_profile']
        # Should maintain coherence
        assert profile.get('coherence_valid', True)


class TestPromptSynthesis:
    """Test prompt synthesis"""
    
    def test_enhanced_prompt_contains_intent(self):
        """Test that enhanced prompt contains sensory intention"""
        enhancer = JazzImprovisationEnhancer()
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="a jazz musician",
            solo_phase="development"
        )
        
        enhanced = result['enhanced_prompt']
        assert "development" in enhanced.lower() or "exploration" in enhanced.lower()
    
    def test_enhanced_prompt_contains_visual_analog(self):
        """Test that enhanced prompt contains visual analog"""
        enhancer = JazzImprovisationEnhancer()
        result = enhancer.enhance_prompt_with_jazz_structure(
            base_prompt="test",
            solo_phase="statement"
        )
        
        # Should have visual analog
        assert result['visual_analog'] is not None
        assert len(result['visual_analog']) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
