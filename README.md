# Jazz Improvisation Structure MCP Server

**Temporal revelation through established grammar—Monk-centered framework**

An MCP (Model Context Protocol) server that translates jazz improvisation structure into visual sensory parameters. Uses rigorous categorical structure (types, morphisms, natural transformations) and intentionality reasoning to enable domain experts to generate images using jazz composition vocabulary.

## Core Premise

Jazz improvisation is **sensory epistemology**—a framework for transmitting harmonic knowledge through temporal reveal. A jazz solo teaches listeners through three phases:

1. **Statement**: Establish the harmonic constraint clearly
2. **Development**: Explore what's possible within that constraint
3. **Resolution**: Integrate learnings and return to clarity

This server maps that three-phase temporal structure to visual sensory parameters, enabling image generation that feels like "knowledge unfolding."

## Architecture

### Layer 1: Categorical Structure (`categorical_structure.yaml`)

Defines the mathematical ontology:

- **Types**: Harmonic Foundation, Intensity Arc, Phrasing Clarity, Temporal Pacing
- **Morphisms**: Statement→Development→Resolution, Harmony→Melody, Constraint→Variation, Clarity-through-Restraint
- **Natural Transformations**: How dimensions scale together
- **Coherence Constraints**: Commutative diagrams ensuring consistency

### Layer 2: Intentionality Reasoning (`intentionality_reasoning.yaml`)

Explains *why* each phase works epistemically:

- Statement: "Clarity entering—listener acquires harmonic roadmap"
- Development: "Complexity revealed as coherent—mastery accumulating"
- Resolution: "Mastery demonstrated through controlled return—integration"

Maps sensory experience to visual analogs and explains the role of Monk-specific principles.

### Layer 3: MCP Implementation

Server provides tools for:
- Enhancing image prompts with jazz structure
- Querying harmonic foundations and phases
- Comparing intensity profiles across phases
- Accessing Monk-specific principles

## Monk-Specific Principles

The server centers on Thelonious Monk because his approach demonstrates perfect understanding of constraint-based innovation:

- **Constraint as Liberation**: Treats harmonic complexity as compositional material
- **Silence as Structure**: Rests are not breaks but intentional elements
- **Rhythmic Displacement**: Behind-the-beat phrasing demonstrates temporal mastery
- **Dissonance as Truth**: Harmonic tension reveals depth, never smoothed away

## Available Tools

### `enhance_prompt_with_jazz`

Enhance an image generation prompt with jazz improvisation aesthetic.

**Parameters:**
- `base_prompt` (required): The original image description
- `harmonic_foundation`: Which Monk composition to anchor ("Round Midnight", "Evidence", "Epistrophy", "Ask Me Now")
- `solo_phase`: Which phase ("statement", "development", "resolution")
- `intensity_level`: 1-10 scale
- `monk_emphasis`: Apply Monk-specific principles (default: true)

**Returns:**
- Enhanced prompt with sensory intention
- Intensity profile (note density, harmonic complexity, rest space, etc.)
- Visual analog and how-it-feels description
- Coherence validation

### `list_harmonic_foundations`

Get all available harmonic foundations with complexity and characteristics.

### `get_harmonic_foundation_details`

Detailed information about a specific foundation including key center and characteristic approach.

### `get_phase_specification`

Get epistemic role, sensory intention, and musical characteristics of a phase.

### `compare_phases_intensity`

Compare intensity profiles (note density, harmonic complexity, etc.) across all three phases.

### `get_monk_principles`

Access Monk-specific anchor principles and how they manifest.

## Harmonic Foundations

All foundations are Thelonious Monk compositions:

| Name | Complexity | Key | Characteristic |
|------|-----------|-----|-----------------|
| Round Midnight | Angular Chromatic | B♭ minor | Tritone substitutions, dissonance as primary material |
| Evidence | Bebop Dense | F major | Rapid harmonic rhythm, precision required |
| Epistrophy | Modal Repetition | E♭ major | Vamp cycles, enables deep exploration |
| Ask Me Now | Lyrical Simple | F major | Sparse changes, melody-driven |

Each foundation has different harmonic complexity, which scales the intensity profile appropriately.

## Intensity Profiles

The server manages three intensity dimensions that respect natural transformations:

### Note Density (1-10)
- 1-3: Sparse, single-note statements
- 5: Balanced note/rest ratio  
- 8-10: Rapid scalar runs, chord arpeggios

### Rhythmic Subdivision (1-10)
- 1-3: Quarter/half note feel
- 5: Eighth note comping
- 8-10: Sixteenth-note figures, polyrhythm

### Harmonic Complexity (1-10)
- 1-3: Root position, simple triads
- 5: Extensions, secondary dominants
- 8-10: Upper extensions, reharmonization, chromatic substitution

### Natural Transformations Applied

1. **Intensity Requires Clarity**: High note density automatically pairs with high rest space
2. **Harmonic Complexity Drives Phrasing**: Dense harmony requires high melodic singularity
3. **Temporal Displacement Needs Anchor**: Behind-the-beat playing requires strong harmonic clarity

## Examples

### Statement Phase Enhancement
```
Base: "a mountain at sunrise"
Phase: statement
Intensity: 3

Enhanced: "a mountain at sunrise, with the sensory character of a 
jazz solo in the statement phase: Clarity entering—the listener 
acquires the harmonic roadmap. Visual treatment: sharp focus, 
established baseline. Intensity profile: restrained, foundational."
```

### Development Phase Enhancement (Monk Emphasis)
```
Base: "a coffee cup"
Harmonic: Evidence (bebop_dense)
Phase: development
Intensity: 7

Enhanced: "a coffee cup, with the sensory character of a jazz solo 
in the development phase: Exploration within constraint—tension 
building, mastery accumulating. Visual treatment: layering, patterns 
visible through texture. Monk principle: Dense layering with clear 
throughlines. Intensity without confusion."
```

### Resolution Phase Enhancement
```
Base: "an empty room"
Phase: resolution
Intensity: 5

Enhanced: "an empty room, with the sensory character of a jazz solo 
in the resolution phase: Return with earned knowledge—integration 
and mastery. Visual treatment: clarity restored, complexity resolved 
into pattern. Precision and confidence."
```

## Installation & Development

### Install for local testing:
```bash
cd jazz-improvisation-mcp
pip install -e .
```

### Run tests:
```bash
pytest tests/ -v
```

### Local MCP server testing:
```bash
python -m jazz_improvisation_mcp.server
```

## Technical Details

### YAML Olog Structure

The categorical structure and intentionality reasoning are stored as YAML "ologs" (ontology logs). This structure:

- Makes the mathematical framework explicit and auditable
- Enables inheritance and extension
- Supports composition with other MCP servers
- Provides clear separation between intent and execution

### Coherence Constraints

All intensity profiles are validated against commutative diagrams to ensure:
- High harmonic complexity pairs with high clarity
- High intensity pairs with high rest space
- Behind-the-beat playing requires harmonic anchor

## Composition with Other MCP Servers

This server can be composed with other aesthetic servers:

- **Cocktail Aesthetics**: Enhance with Monk + your favorite cocktail
- **Slapstick Comedy**: Combine temporal revelation with physical comedy
- **Perfume Aesthetics**: Map harmonic phases to scent structure

## On-the-Horizon Extensions

- **Modal Expansion**: Add other jazz traditions (Coltrane modal harmony, free jazz)
- **Temporal Pacing**: Explicit control over how fast phases unfold
- **Voice Composition**: Support for multiple improvising voices (piano + bass + drums interaction)
- **Harmonic Deviation Analysis**: Quantify how far development strays from constraint

## Key Learnings

1. **Domain expertise contains visual information**: Jazz structure encodes how knowledge reveals through time. This isn't metaphorical—it's structural.

2. **Constraint enables variation**: The harmonic foundation isn't a limitation—it's the *floor* from which mastery emerges. Higher constraints enable richer variation.

3. **Silence is active**: Rests aren't absences but structural elements. High complexity requires high rest space for legibility.

4. **Temporal structure matters**: This system requires time. You can't transmit harmonic knowledge all at once—constraint, variation, integration must sequence.

5. **Monk as anchor**: Monk's approach perfectly demonstrates constraint-as-liberation. His angular harmony, behind-the-beat pacing, and intentional silence show that mastery *is* the ability to work precisely within constraint.

## References

- Thelonious Monk's recordings and compositions
- Category theory and natural transformations
- Cognitive science of temporal sensory revelation
- Jazz pedagogy and harmonic analysis

## License

MIT

## Author

Dal (@dmarsters)
