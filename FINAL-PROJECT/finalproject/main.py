# Task-1: Load historical data from orcl.csv into a list of dictionaries
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        # Skip the header row
        header = file.readline().strip().split(',')
        
        for line in file:
            values = line.strip().split(',')
            # Create a dictionary for each row
            row_dict = {header[i]: values[i] for i in range(len(header))}
            data.append(row_dict)
            
    return data

# Task-2: Calculate Simple Moving Averages (SMA) and Relative Strength Index (RSI)
def calculate_indicators(data):
    # Initialize lists to store SMA and RSI values
    sma_values = []
    rsi_values = []

    for i in range(len(data)):
        # Calculate SMA for the 5-day window
        if i >= 4:
            close_prices = [float(data[j]['Close']) for j in range(i-4, i+1)]
            sma = sum(close_prices) / 5
            sma_values.append(sma)
        
        # Calculate RSI for the 14-day window
        if i >= 13:
            gains = losses = 0
            for j in range(i-13, i):
                price_diff = float(data[j+1]['Close']) - float(data[j]['Close'])
                if price_diff > 0:
                    gains += price_diff
                else:
                    losses += abs(price_diff)
            
            avg_gain = gains / 14
            avg_loss = losses / 14

            # Check if both avg_gain and avg_loss are zero
            if avg_gain == 0 and avg_loss == 0:
                rsi = 50  # Set RSI to 50 in this case
            else:
                # Check if avg_loss is zero or close to zero
                if avg_loss != 0 and avg_loss > 1e-10:
                    rs = avg_gain / avg_loss
                    rsi = 100 - (100 / (1 + rs))
                else:
                    # Handle the case where avg_loss is zero or close to zero
                    rsi = 100
            rsi_values.append(rsi)
    
    return sma_values, rsi_values

# Task-3: Write indicators to files
def write_to_file(file_path, values, header):
    with open(file_path, 'w') as file:
        # Write header
        file.write(','.join(header) + '\n')
        # Write data
        for value in values:
            file.write(str(value) + '\n')



def main():
    # File paths
    input_file_path = 'data/orcl.csv'
    sma_file_path = 'data/orcl-sma.csv'
    rsi_file_path = 'data/orcl-rsi.csv'

    # Load data from the CSV file
    historical_data = load_data(input_file_path)

    # Calculate indicators
    sma_values, rsi_values = calculate_indicators(historical_data)

    # Write SMA values to file
    write_to_file(sma_file_path, sma_values, ['SMA'])

    # Write RSI values to file
    write_to_file(rsi_file_path, rsi_values, ['RSI'])

    print("Done!... YOU NAILED IT LINA!")


if __name__ == "__main__":
    
    main()