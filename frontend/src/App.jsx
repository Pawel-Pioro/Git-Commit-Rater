import { useState } from 'react'
import axios from 'axios'

function App({ baseUrl }) {
  const [scenario, setScenario] = useState({
    "scenario": "",
    "key": 0
  })
  const [message, setMessage] = useState('')
  const [result, setResult] = useState('')
  const [userInput, setUserInput] = useState({
    topic: '',
    language: ''
  })

  const commit = () => {
    if (message) {
      axios.post(baseUrl + "commit-message/", { "commit_message": message, "key": scenario.key })
        .then((res) => {
          setResult(res.data.feedback)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }

  const generateScenario = () => {
    if (userInput.topic && userInput.language) {
      axios.post(baseUrl + "scenario/", userInput)
        .then((res) => {
          setScenario(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }

  return (
    <div className="container mt-5">
      <h1 className="text-center">Git Commit Rater</h1>

      {scenario.scenario === '' ?
        <div>
          <div className='input-group mb-3'>
            <span className="input-group-text" id="inputGroup-sizing-default">Enter a topic</span>
            <input value={userInput.topic} onChange={(e) => setUserInput({ ...userInput, topic: e.target.value })} type="text" className="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" />
          </div>
          <div className='input-group mb-3'>
            <span className="input-group-text" id="inputGroup-sizing-default">Enter a programming language</span>
            <input value={userInput.language} onChange={(e) => setUserInput({ ...userInput, language: e.target.value })} type="text" className="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" />
          </div>
          <button
            className="btn btn-primary "
            style={{ width: '100%' }}
            onClick={() => generateScenario()}
          >
            Generate Scenario
          </button>
        </div>
        :
        <>
          <div id='scenario'>
            <p style={{ "whiteSpace": "pre-wrap" }}>{scenario.scenario}</p>
          </div>
          <hr />
          <div id="messageDiv">
            <h3>Enter your commit message for the scenario</h3>
            <input id="messageInput" type="text" className='form-control' onChange={(e) => setMessage(e.target.value)} value={message} />
            <button
              className="btn btn-primary mt-3"
              style={{ width: '100%' }}
              onClick={() => {
                commit()
              }}
            >
              Commit
            </button>
          </div>
          {result &&
            <>
              <br />
              <h3>{result}</h3>
            </>
          }
        </>
      }
    </div >
  )
}

export default App
