# AgentsVille Trip Planner

An AI-powered travel planning system that demonstrates advanced LLM reasoning techniques including role-based prompting, chain-of-thought reasoning, ReAct prompting, reflexion, and memory management.

## Project Overview

The AgentsVille Trip Planner is a Jupyter Notebook-based application that creates personalized travel itineraries using multiple AI agents working together. The system simulates external API calls to gather weather data, cultural events, restaurants, and activities, then processes this information to create customized travel plans based on group size, ages, interests, and other constraints.

## Key Features

### 🤖 Multi-Agent Architecture
- **BoolResponseAgent**: Handles yes/no questions with self-consistency prompting
- **ChatAgent**: Base conversational agent with memory management
- **Traveler Agent**: Simulates user interactions for testing
- **OnboardingAgent**: Gathers vacation information from travelers
- **ItineraryAgent**: Generates initial travel itineraries using ReAct cycles
- **ItineraryRevisionAgent**: Refines itineraries based on feedback and evaluations

### 🧠 Advanced LLM Techniques
- **Role-Based Prompting**: Specialized travel planner personas
- **Chain-of-Thought Reasoning**: Step-by-step planning processes
- **ReAct Prompting**: Thought → Action → Observation cycles
- **Reflexion**: Self-evaluation to correct mistakes and improve plans
- **Memory Management**: Maintaining context about user preferences

### 🛠️ Tool Integration
- **Weather API**: Simulated weather data retrieval
- **Events API**: Cultural and activity information
- **Cost Calculator**: Accurate budget calculations
- **Evaluation Tools**: Quality assessment and feedback

### 📊 Comprehensive Evaluation System
- City and date validation
- Cost accuracy verification
- Interest matching and balance assessment
- Weather compatibility checks
- Dietary restriction compliance

## Project Structure

```
agentsVille project/
├── project_starter.ipynb    # Main Jupyter notebook with agent implementations
├── project_lib.py          # Helper functions and utility classes
├── .gitignore              # Git ignore file for Python cache
└── README.md               # This file
```

## Setup Instructions

### Prerequisites
- Python 3.13+
- Jupyter Notebook
- OpenAI API key

### Installation

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd "agentsVille project"
   ```

2. **Install dependencies**
   ```bash
   pip install openai==1.74.0
   ```

3. **Configure OpenAI API Key**
   - Set your OpenAI API key as an environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Or configure it in your Jupyter notebook

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

5. **Open the project notebook**
   - Open `project_starter.ipynb` in Jupyter

## Usage

### 1. Define Vacation Details
The system uses a structured approach to gather vacation information:

```python
vacation_info = {
    "travelers": [
        {
            "name": "Yuri",
            "age": 30,
            "interests": ["tennis", "cooking"],
            "dietary_restrictions": ["nut allergies"],
        },
        {
            "name": "Hiro", 
            "age": 25,
            "interests": ["reading", "music"],
            "dietary_restrictions": ["vegetarian"],
        },
    ],
    "destination": "AgentsVille",
    "date_of_arrival": "2025-06-10",
    "date_of_departure": "2025-06-11", 
    "budget": 1000,
}
```

### 2. Run the Complete Planning Process

```python
# Create agents
onboarding_agent = OnboardingAgent()
traveler = Traveler(template_kwargs={"vacation_info": vacation_info})
itinerary_agent = ItineraryAgent()
revision_agent = ItineraryRevisionAgent()

# Gather information
gathered_info = onboarding_agent.gather_vacation_info(traveler_agent=traveler)

# Generate initial itinerary
initial_itinerary = itinerary_agent.get_itinerary(vacation_info=gathered_info)

# Evaluate and revise
final_itinerary = revision_agent.get_itinerary(
    vacation_info=gathered_info,
    proposed_itinerary=initial_itinerary
)
```

### 3. Evaluation and Quality Assurance

The system includes comprehensive evaluation functions:

- **City and Date Validation**: Ensures itinerary matches requested destination and dates
- **Cost Accuracy**: Verifies total cost calculations match activity prices
- **Interest Matching**: Checks that activities align with traveler interests
- **Weather Compatibility**: Ensures outdoor activities aren't scheduled during inclement weather
- **Dietary Compliance**: Validates that food activities respect dietary restrictions

## Core Components

### BoolResponseAgent
Handles yes/no questions with multiple LLM calls for consensus:
```python
bool_agent = BoolResponseAgent()
response = bool_agent.get_response("Is this activity suitable for children?", num_calls=3)
```

### ChatAgent
Base conversational agent with memory and context management:
```python
chat_agent = ChatAgent("TravelPlanner")
response = chat_agent.chat("What activities are available today?")
```

### ItineraryAgent
Generates travel itineraries using ReAct cycles:
- **Thought**: Reasoning about available options
- **Action**: Tool calls to gather data (weather, events)
- **Observation**: Processing tool results
- **Final Output**: Structured itinerary in JSON format

### ItineraryRevisionAgent
Refines itineraries based on evaluation feedback:
- Incorporates user feedback
- Runs evaluation tools
- Iteratively improves the plan
- Ensures all constraints are met

## Evaluation Criteria

The project is assessed based on:

1. **Prompt Design Quality**: System prompts that consistently produce valid JSON output
2. **ReAct Implementation**: Proper THOUGHT-ACTION-OBSERVATION cycles
3. **Tool Integration**: Valid tool calls in specified JSON format
4. **Evaluation Success**: Final itineraries that pass all evaluation criteria
5. **Constraint Satisfaction**: Plans that respect interests, weather, and dietary restrictions

## Success Metrics

A successful implementation will:

- ✅ Generate JSON output that validates against the TravelPlan Pydantic model
- ✅ Produce itineraries that reflect user preferences accurately
- ✅ Implement proper ReAct cycles with valid tool calls
- ✅ Pass all evaluation criteria consistently
- ✅ Incorporate user feedback effectively
- ✅ Handle edge cases and constraints appropriately

## Technical Implementation

### Pydantic Models
The system uses Pydantic for data validation and structure:
- `VacationInfo`: Traveler details and trip constraints
- `TravelPlan`: Structured itinerary output format

### Tool System
Four main tools support the agents:
- `calculator_tool`: Cost calculations
- `get_activities_by_date_tool`: Activity retrieval
- `run_evals_tool`: Evaluation execution
- `final_answer_tool`: Structured output generation

### JSON Parsing
Robust JSON extraction from LLM outputs with retry logic for malformed responses.

## Fun Features

The system includes a narrative trip summary that creates engaging stories about the planned vacation, highlighting the best activities and experiences!

## Contributing

This is an educational project demonstrating AI agent development techniques. The focus is on prompt engineering, agent interaction patterns, and evaluation methodologies.

## License

This project is for educational purposes as part of the AgentsVille course curriculum.

---

**Happy Travel Planning! 🗺️✈️** 