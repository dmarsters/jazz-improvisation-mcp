"""
Jazz Improvisation Structure MCP Server
Temporal revelation through established grammar - Monk-centered framework
"""

from fastmcp import FastMCP
from jazz_improvisation_mcp.enhancer import JazzImprovisationEnhancer
from jazz_improvisation_mcp.olog_loader import JazzImprovisationOlog

# Initialize FastMCP server
mcp = FastMCP("jazz-improvisation-mcp")
enhancer = JazzImprovisationEnhancer()
olog = JazzImprovisationOlog()


@mcp.tool()
def enhance_prompt_with_jazz(
    base_prompt: str,
    harmonic_foundation: str = "Round Midnight",
    solo_phase: str = "development",
    intensity_level: int = 5,
    monk_emphasis: bool = True,
) -> dict:
    """
    Enhance an image generation prompt with jazz improvisation aesthetic.
    
    Args:
        base_prompt: The original image description to enhance
        harmonic_foundation: Which Monk composition to anchor (Round Midnight, Evidence, Epistrophy, Ask Me Now)
        solo_phase: Which phase of solo structure (statement, development, resolution)
        intensity_level: Intensity scale 1-10
        monk_emphasis: Emphasize Monk-specific principles
    
    Returns:
        Enhanced prompt with jazz structure parameters
    """
    return enhancer.enhance_prompt_with_jazz_structure(
        base_prompt=base_prompt,
        harmonic_foundation=harmonic_foundation,
        solo_phase=solo_phase,
        intensity_level=intensity_level,
        monk_emphasis=monk_emphasis,
    )


@mcp.tool()
def list_harmonic_foundations() -> dict:
    """List all available harmonic foundations (Monk compositions)."""
    foundations = enhancer.get_all_harmonic_foundations()
    return {
        "foundations": [
            {
                "name": f["name"],
                "complexity": f["complexity"],
                "key_center": f["key_center"],
                "characteristic": f["characteristic"],
                "monk_essence": f.get("monk_essence", False),
            }
            for f in foundations
        ]
    }


@mcp.tool()
def get_harmonic_foundation_details(foundation_name: str) -> dict:
    """
    Get detailed information about a specific harmonic foundation.
    
    Args:
        foundation_name: Name of the harmonic foundation
    
    Returns:
        Foundation details including complexity, key center, and characteristics
    """
    foundation = olog.get_harmonic_foundation(foundation_name)
    if not foundation:
        return {"error": f"Foundation '{foundation_name}' not found"}
    return {
        "name": foundation["name"],
        "complexity": foundation["complexity"],
        "key_center": foundation["key_center"],
        "characteristic": foundation["characteristic"],
        "monk_essence": foundation.get("monk_essence", False),
    }


@mcp.tool()
def get_phase_specification(phase_name: str) -> dict:
    """
    Get detailed specification for a solo phase.
    
    Args:
        phase_name: Which solo phase to get specification for (statement, development, resolution)
    
    Returns:
        Phase specification including narrative role and sensory intention
    """
    phase_spec = olog.get_phase_specification(phase_name)
    if not phase_spec:
        return {"error": f"Phase '{phase_name}' not found"}
    return {
        "phase": phase_name,
        "narrative_role": phase_spec.get("narrative_role"),
        "sensory_intention": phase_spec.get("sensory_intention"),
        "what_happens_musically": phase_spec.get("what_happens_musically"),
    }


@mcp.tool()
def compare_phases_intensity(harmonic_foundation: str = "Round Midnight") -> dict:
    """
    Compare intensity profiles across all three solo phases.
    
    Args:
        harmonic_foundation: Which harmonic foundation to use for comparison
    
    Returns:
        Intensity comparison across statement, development, and resolution phases
    """
    profiles = enhancer.compare_phases_intensity(harmonic_foundation)
    return {
        "harmonic_foundation": harmonic_foundation,
        "phase_comparison": {
            phase: {
                k: v
                for k, v in profile.items()
                if k
                in [
                    "note_density",
                    "rhythmic_subdivision",
                    "harmonic_complexity",
                    "melodic_singularity",
                    "rest_space",
                ]
            }
            for phase, profile in profiles.items()
        },
    }


@mcp.tool()
def get_monk_principles() -> dict:
    """Get Monk-specific anchor principles."""
    principles = olog.get_monk_principles()
    return {
        "principles": {
            name: {
                "statement": principle.get("statement"),
                "manifests_as": principle.get("manifests_as"),
            }
            for name, principle in principles.items()
        }
    }

if __name__ == "__main__":
    mcp.run()
