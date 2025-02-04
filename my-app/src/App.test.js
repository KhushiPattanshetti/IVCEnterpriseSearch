"IVC Ventures International Innovation Pvt Ltd (IVC Ventures) Confidential."
 "No license grant and not for distribution of any nature. All Rights Reserved."
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
