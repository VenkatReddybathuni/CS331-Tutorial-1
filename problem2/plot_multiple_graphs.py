import matplotlib.pyplot as plt
import os

def create_results_dir():
    results_dir = "server_graphs"
    os.makedirs(results_dir, exist_ok=True)
    return results_dir

def plot_single_server(client_counts, times, results_dir):
    plt.figure(figsize=(10, 6))
    plt.plot(client_counts, times, 'o-', color='blue', linewidth=2, markersize=8)
    
    # Add value labels
    for x, y in zip(client_counts, times):
        plt.annotate(f'{y:.2f}s', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Number of Concurrent Clients', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Single-Process Server Performance', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.savefig(os.path.join(results_dir, 'single_process.png'), dpi=300, bbox_inches='tight')
    plt.close()

def plot_multi_process(client_counts, times, results_dir):
    plt.figure(figsize=(10, 6))
    plt.plot(client_counts, times, 's-', color='red', linewidth=2, markersize=8)
    
    for x, y in zip(client_counts, times):
        plt.annotate(f'{y:.2f}s', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Number of Concurrent Clients', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Multi-Process Server Performance', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.savefig(os.path.join(results_dir, 'multi_process.png'), dpi=300, bbox_inches='tight')
    plt.close()

def plot_multi_thread(client_counts, times, results_dir):
    plt.figure(figsize=(10, 6))
    plt.plot(client_counts, times, '^-', color='green', linewidth=2, markersize=8)
    
    for x, y in zip(client_counts, times):
        plt.annotate(f'{y:.2f}s', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Number of Concurrent Clients', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Multi-Threaded Server Performance', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.savefig(os.path.join(results_dir, 'multi_thread.png'), dpi=300, bbox_inches='tight')
    plt.close()

def plot_comparison(client_counts, single_times, multi_process_times, multi_thread_times, results_dir):
    plt.figure(figsize=(12, 8))
    
    plt.plot(client_counts, single_times, 'o-', color='blue', 
            label='Single-Process', linewidth=2, markersize=8)
    plt.plot(client_counts, multi_process_times, 's-', color='red', 
            label='Multi-Process', linewidth=2, markersize=8)
    plt.plot(client_counts, multi_thread_times, '^-', color='green', 
            label='Multi-Thread', linewidth=2, markersize=8)
    
    for x, y1, y2, y3 in zip(client_counts, single_times, multi_process_times, multi_thread_times):
        plt.annotate(f'{y1:.2f}s', (x, y1), textcoords="offset points", xytext=(0,10), ha='center')
        plt.annotate(f'{y2:.2f}s', (x, y2), textcoords="offset points", xytext=(0,10), ha='center')
        plt.annotate(f'{y3:.2f}s', (x, y3), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('Number of Concurrent Clients', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Server Performance Comparison', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    plt.savefig(os.path.join(results_dir, 'comparison.png'), dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Your measurement data
    client_counts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    single_times = [30.03, 59.31, 90.03, 120.06, 150.1, 182.06, 213.15, 245.05, 273.14, 304.2]
    multi_process_times = [3.05, 3.09, 3.14, 3.17, 3.21, 3.27, 4.3, 5.39, 5.43, 5.47]
    multi_thread_times = [3.05, 3.08, 4.15, 4.15, 4.23, 4.24, 4.51, 4.54, 4.56, 5.37]
    
    # Create results directory and save all plots
    results_dir = create_results_dir()
    
    # Generate individual plots
    plot_single_server(client_counts, single_times, results_dir)
    plot_multi_process(client_counts, multi_process_times, results_dir)
    plot_multi_thread(client_counts, multi_thread_times, results_dir)
    plot_comparison(client_counts, single_times, multi_process_times, multi_thread_times, results_dir)
    
    print(f"\nGraphs have been saved in the directory: {results_dir}")
    print("Generated files:")
    print("1. single_process.png")
    print("2. multi_process.png")
    print("3. multi_thread.png")
    print("4. comparison.png")
