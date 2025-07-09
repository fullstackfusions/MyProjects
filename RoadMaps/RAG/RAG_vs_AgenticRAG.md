![RAG vs Agentic RAG](/assets/RAG_vs_AgentincRAG.jpeg "RAG vs Agentic RAG")

---

## 🔹 Classic RAG (Top Panel)

1. **User → Prompt & Query**
   The user enters a question or prompt in an LLM-powered interface.

2. **Server Issues a Retrieval Query**
   The backend sends that query off to a search service.

3. **Search & Fetch from Knowledge Sources**
   The search layer pulls in relevant bits from PDFs, databases, documents, code repos, web search or APIs.

4. **Return “Enhanced Context”**
   Those retrieved passages are sent back to the server.

5. **LLM Prompting with Context**
   The server stitches together your original prompt + retrieved context and forwards that to an LLM (GPT, Gemini, Claude).

6. **Generated Text Response → User**
   The model generates an answer using both your prompt and the retrieved snippets.

---

## 🔹 Agentic RAG (Bottom Panel)

1. **User → Prompt & Query**
   Same as above.

2. **Query → Aggregator Agent**
   Instead of a simple server, an “Aggregator Agent” takes ownership of the request.

3. **Planning & Memory**
   The agent builds a multi-step plan (using CoT/ReACT) and may draw on short-term or long-term memory.

4. **Dispatch to Multiple Specialized Agents**
   The plan spawns sub-agents, for example:

   * **Agent 1** querying local data (via an MCP server)
   * **Agent 2** running web searches
   * **Agent 3** calling cloud engines (AWS/Azure)

5. **Aggregate Enhanced Context**
   Each sub-agent fetches its slice of information and reports back to the aggregator, which collates everything plus any relevant memory.

6. **LLM Generation → User**
   The aggregator then prompts the LLM (GPT/Gemini/Claude) with the full, enriched context to produce a final response.

---

### Key Takeaways

* **Classic RAG** is essentially a two-step retrieve → generate pipeline.
* **Agentic RAG** layers in:

  * A planner/aggregator
  * Multiple specialized fetch-agents
  * Memory (short & long term)
  * A more complex, multi-hop workflow before generation

This “agentic” approach can handle richer orchestrations—tool use, branching logic, cost/latency trade-offs—rather than just “fetch vectors + send to LLM.”
