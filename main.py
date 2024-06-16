# main.py
from ReeseAGI import CognitiveArchitecture

def main():
    # Create instances of components
    knowledge_graph = KnowledgeGraph()
    reasoning_engine = ReasoningEngine(knowledge_graph)
    self_improvement_mechanism = SelfImprovementMechanism(knowledge_graph)
    quantum_ai_component = QuantumAIComponent()
    cognitive_architecture = CognitiveArchitecture(knowledge_graph, reasoning_engine, self_improvement_mechanism, quantum_ai_component)

    # Process input data
    input_data = {
        'entities': [
            {'id': 'AAPL', 'properties': ['high', 'low', 'close'], 'relationships': [{'id': '1', 'type': 'causes', 'target': 'buy'}]}
        ],
        'outcome': 'profit'
    }
    decision = cognitive_architecture.process_input(input_data)
    print(f"Decision: {decision}")
    print(f"Accuracy: {cognitive_architecture.get_accuracy():.2f}")

if __name__ == "__main__":
    main()