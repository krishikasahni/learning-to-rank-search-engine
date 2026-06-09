import React, { useState } from "react";
import Autocomplete from "../components/Autocomplete";

function SearchPage() {
const [query, setQuery] = useState("");
const [results, setResults] = useState([]);
const [suggestions, setSuggestions] = useState([]);
const [loading, setLoading] = useState(false);

const API_URL = "https://learning-to-rank-search-engine.onrender.com";

const fetchSuggestions = async (value) => {
if (!value) {
setSuggestions([]);
return;
}

try {
  const response = await fetch(
    `${API_URL}/autocomplete?q=${encodeURIComponent(value)}`
  );

  const data = await response.json();
  setSuggestions(data.suggestions || []);
} catch (error) {
  console.error(error);
}

};

const sendFeedback = async (title) => {
try {
await fetch(`${API_URL}/feedback`, {
method: "POST",
headers: {
"Content-Type": "application/json",
},
body: JSON.stringify({
query,
title,
}),
});
} catch (err) {
console.error(err);
}
};

const handleSearch = async () => {
if (!query.trim()) return;

setLoading(true);

try {
  const response = await fetch(
    `${API_URL}/search`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        query,
      }),
    }
  );

  const data = await response.json();

  setResults(data.results || []);
  setSuggestions([]);
} catch (error) {
  console.error(error);
  alert("Backend connection failed");
} finally {
  setLoading(false);
}

};

return (
<div
style={{
maxWidth: "1000px",
margin: "0 auto",
padding: "40px",
fontFamily: "Arial",
}}
> <h1>
Hybrid Learning-to-Rank
Search Engine </h1>

  <div
    style={{
      marginBottom: "30px",
      position: "relative",
    }}
  >
    <input
      type="text"
      placeholder="Enter search query"
      value={query}
      onChange={(e) => {
        setQuery(e.target.value);
        fetchSuggestions(
          e.target.value
        );
      }}
      style={{
        padding: "12px",
        width: "350px",
        marginRight: "10px",
        borderRadius: "8px",
        border: "1px solid #ccc",
      }}
    />

    <button
      onClick={handleSearch}
      style={{
        padding: "12px 20px",
        cursor: "pointer",
        borderRadius: "8px",
      }}
    >
      Search
    </button>

    <Autocomplete
      suggestions={suggestions}
      onSelect={(text) => {
        setQuery(text);
        setSuggestions([]);
      }}
    />
  </div>

  {loading && (
    <h3>🔍 Searching...</h3>
  )}

  {!loading &&
    results.length > 0 && (
      <>
        <div
          style={{
            backgroundColor:
              "#fff7ed",
            border:
              "2px solid #f59e0b",
            borderRadius:
              "12px",
            padding: "20px",
            marginBottom:
              "25px",
          }}
        >
          <h2>
            🏆 Top Ranked Result
          </h2>

          <h3>
            {results[0].title}
          </h3>

          <p>
            {results[0].content}
          </p>

          <strong>
            Hybrid Score:{" "}
            {
              results[0]
                .hybrid_score
            }
          </strong>
        </div>

        <h3>
          Found {results.length}{" "}
          results
        </h3>
      </>
    )}

  {!loading &&
  results.length > 0 ? (
    results.map((item, index) => (
      <div
        key={index}
        style={{
          border:
            "1px solid #ddd",
          borderRadius: "12px",
          padding: "20px",
          marginBottom: "20px",
          backgroundColor: "#fff",
          boxShadow:
            "0 2px 8px rgba(0,0,0,0.1)",
        }}
      >
        <h3
          style={{
            color: "#666",
            marginBottom: "5px",
          }}
        >
          #{index + 1}
        </h3>

        <h2>{item.title}</h2>

        <p>{item.content}</p>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "10px",
            marginTop: "15px",
            marginBottom:
              "15px",
          }}
        >
          <span
            style={{
              padding:
                "8px 12px",
              backgroundColor:
                "#eef2ff",
              borderRadius:
                "20px",
            }}
          >
            🎯 Semantic:{" "}
            {
              item.semantic_score
            }
          </span>

          <span
            style={{
              padding:
                "8px 12px",
              backgroundColor:
                "#ecfeff",
              borderRadius:
                "20px",
            }}
          >
            📊 BM25:{" "}
            {item.bm25_score}
          </span>

          <span
            style={{
              padding:
                "8px 12px",
              backgroundColor:
                "#f0fdf4",
              borderRadius:
                "20px",
            }}
          >
            👆 Clicks:{" "}
            {item.click_score}
          </span>

          <span
            style={{
              padding:
                "8px 12px",
              backgroundColor:
                "#fef3c7",
              borderRadius:
                "20px",
            }}
          >
            🤖 ML:{" "}
            {item.ml_score}
          </span>

          <span
            style={{
              padding:
                "8px 12px",
              backgroundColor:
                "#fee2e2",
              borderRadius:
                "20px",
              fontWeight:
                "bold",
            }}
          >
            ⭐ Hybrid:{" "}
            {item.hybrid_score}
          </span>
        </div>

        <button
          onClick={() =>
            sendFeedback(
              item.title
            )
          }
          style={{
            padding:
              "10px 20px",
            cursor: "pointer",
            borderRadius: "8px",
          }}
        >
          Open Result
        </button>
      </div>
    ))
  ) : (
    !loading && (
      <p>
        Search for something
        to see results.
      </p>
    )
  )}
</div>

);
}

export default SearchPage;
