// Sample data (replace with your 1400 values)
const data = [
  { "value": "Value1", "description": "Description for Value1" },
  { "value": "Value2", "description": "Description for Value2" },
  // ... (1400 entries)
];

const valuesContainer = document.getElementById('values-container');

// Populate values
data.forEach(item => {
  const valueCard = document.createElement('div');
  valueCard.classList.add('value-card');
  valueCard.textContent = item.value;

  // Add click event to show description
  valueCard.addEventListener('click', () => {
    alert(item.description); // You can replace this with a modal or redirect to a new page
  });

  valuesContainer.appendChild(valueCard);
});
