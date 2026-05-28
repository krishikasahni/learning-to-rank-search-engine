import { useState } from 'react'
import axios from 'axios'

export default function Home() {

  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])

  const handleSearch = async () => {
    const response = await axios.get(
      `http://localhost:8000/search/?query=${query}`
    )

    setResults(response.data.results)
  }

  return (
    <div style={{padding: '40px'}}>
      <h1>LTR Search Engine</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search"
      />

      <button onClick={handleSearch}>
        Search
      </button>

      {results.map((result, index) => (
        <div key={index}>
          <h3>Result #{index + 1}</h3>
          <p>{result.content}</p>
          <p>Score: {result.ltr_score}</p>
        </div>
      ))}
    </div>
  )
}