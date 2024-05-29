import { useState } from 'react'

function App() {
  const [scenario, setScenario] = useState({})
  const [message, setMessage] = useState('')

  return (
    <div className="container">
      <h1 className="text-center">Git Commit Rater</h1>

      {Object.keys(scenario).length === 0 ?
        <div>
          <button
            className="btn btn-primary"
            onClick={() => setScenario({ scenario: 'Hello World', code: 'console.log("Hello World")' })}
          >
            Generate Scenario
          </button>
        </div>
        :
        <>
          <div id='scenario'>
            <h2>{scenario.scenario}</h2>
            <p>{scenario.code}</p>
          </div>
          <hr />
          <div id="messageDiv">
            <h3>Enter your commit message for the scenario</h3>
            <input id="messageInput" type="text" className='form-control' />
            <button
              className="btn btn-primary "
              onClick={() => {
                setScenario({ ...scenario, message: document.getElementById('messageInput').value })
              }}
            >
              Commit
            </button>
          </div>
        </>
      }
    </div>
  )
}

export default App
