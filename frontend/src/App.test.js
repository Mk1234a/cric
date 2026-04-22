import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import store from './store';
import App from './App';

test('renders app header', () => {
  render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  const headerElements = screen.getAllByText(/Auction/i);
  expect(headerElements.length).toBeGreaterThan(0);
});