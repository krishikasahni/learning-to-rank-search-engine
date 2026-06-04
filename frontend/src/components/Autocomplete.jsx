import React from "react";

function Autocomplete({ suggestions, onSelect }) {
  if (!suggestions.length) return null;

  return (
    <div
      style={{
        width: "300px",
        border: "1px solid #ccc",
        borderTop: "none",
        background: "white",
        position: "absolute",
        zIndex: 1000,
      }}
    >
      {suggestions.map((item, index) => (
        <div
          key={index}
          onClick={() => onSelect(item)}
          style={{
            padding: "10px",
            cursor: "pointer",
            borderBottom: "1px solid #eee",
          }}
        >
          {item}
        </div>
      ))}
    </div>
  );
}

export default Autocomplete;