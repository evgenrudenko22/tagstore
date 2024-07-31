import { useEffect, useState } from 'react'
import axios from 'axios'
import styles from "./App.module.css"

function App() {
  const [items, setItems] = useState(null)

  const fetchItems = () => {
    axios.get('http://185.198.165.177:8080/api/items').then(r => {
      setItems(r.data)
    })
  }

  useEffect(() => {
    fetchItems()
    setInterval(() => {
      fetchItems()
    }, 2000)
  }, [])

  return (
    <>
      <div className={styles.items}>
        {items && items.map(item => {
          return <span className={styles.item} key={item.id}>
            <span>{item.name}</span>
          </span>
        })}
      </div>
    </>
  )
}

export default App
