import sys
from data_loader import get_simulation_data
# from algorithms import solve_greedy_tsp
from algorithms import solve_exact_tsp
from cost_calculator import calculate_tco

def main():
    try:
        matrix, weights, names, config_data = get_simulation_data()
    except Exception as e:
        print(f"Error saat memuat data: {e}")
        sys.exit(1)
        
    price_subsidy = config_data['skenario_bbm']['subsidi']['harga_bbm_per_liter']
    price_crisis = config_data['skenario_bbm']['krisis']['harga_bbm_per_liter']
    
    print("=" * 90)
    print(" PIPELINE SIMULASI KOMPASARI OPERASIONAL LAST-MILE DELIVERY")
    print(f" [Skenario Subsidi: Rp {price_subsidy:,}/L] | [Skenario Krisis: Rp {price_crisis:,}/L]")
    print("=" * 90)

    # uncomment kalo udah ada fungsinya     
    # route_a, exec_time_a = solve_greedy_tsp(matrix)
    # dist_a = sum(matrix[route_a[i]][route_a[i+1]] for i in range(len(route_a)-1))

    route_b, exec_time_b = solve_exact_tsp(matrix)
    dist_b = sum(matrix[route_b[i]][route_b[i+1]] for i in range(len(route_b)-1))
    
    # --- Skenario Subsidi ---
    # uncomment kalo udah ada fungsinya     
    # fuel_a_sub, server_a_sub, tco_a_sub = calculate_tco(route_a, matrix, weights, price_subsidy, config_data, exec_time_a)
    fuel_b_sub, server_b_sub, tco_b_sub = calculate_tco(route_b, matrix, weights, price_subsidy, config_data, exec_time_b)
    
    # --- Skenario Krisis ---
    # uncomment kalo udah ada fungsinya     
    # fuel_a_cri, server_a_cri, tco_a_cri = calculate_tco(route_a, matrix, weights, price_crisis, config_data, exec_time_a)
    fuel_b_cri, server_b_cri, tco_b_cri = calculate_tco(route_b, matrix, weights, price_crisis, config_data, exec_time_b)

    print(f"\n{"METRIK SIMULASI FILTRASI":<24} | {"SKENARIO SUBSIDI (Rp 5.000)":<30} | {"SKENARIO KRISIS (Rp 20.000)":<30}")
    print(f"{"":<24} | {"Algo A (Heuristik)":<14} {"Algo B (Eksak)":<15} | {"Algo A (Heuristik)":<14} {"Algo B (Eksak)":<15}")
    print("-" * 92)
    
    # uncomment kalo udah ada fungsinya     
    # print(f"{"Waktu Eksekusi Presisi":<24} | {f"{exec_time_a:.3f} ms":<14} {f"{exec_time_b:.3f} ms":<15} | {f"{exec_time_a:.3f} ms":<14} {f"{exec_time_b:.3f} ms":<15}")
    # print(f"{"Total Jarak Fisik Rute":<24} | {f"{dist_a:.2f} km":<14} {f"{dist_b:.2f} km":<15} | {f"{dist_a:.2f} km":<14} {f"{dist_b:.2f} km":<15}")
    # print("-" * 92)
    
    # print(f"{"Rincian Biaya BBM":<24} | {f"Rp {fuel_a_sub:,.0f}":<14} {f"Rp {fuel_b_sub:,.0f}":<15} | {f"Rp {fuel_a_cri:,.0f}":<14} {f"Rp {fuel_b_cri:,.0f}":<15}")
    # print(f"{"Rincian Biaya Server":<24} | {f"Rp {server_a_sub:,.0f}":<14} {f"Rp {server_b_sub:,.0f}":<15} | {f"Rp {server_a_cri:,.0f}":<14} {f"Rp {server_b_cri:,.0f}":<15}")
    # print("-" * 92)
    
    # print(f"{"TOTAL VALUE TCO":<24} | \033[1;32mRp {tco_a_sub:,.0f}\033[0m{"":<4} \033[1;31mRp {tco_b_sub:,.0f}\033[0m{"":<5} | \033[1;31mRp {tco_a_cri:,.0f}\033[0m{"":<4} \033[1;32mRp {tco_b_cri:,.0f}\033[0m")
    # print("=" * 92)
    
    print("\n[DETAIL URUTAN RUTE UNTUK KEDUANYA]")
    # uncomment kalo udah ada fungsinya     
    # print(f"• Rute Algo A (Heuristik) : {' -> '.join([names[i] for i in route_a])}")
    print(f"• Rute Algo B (Eksak)     : {' -> '.join([names[i] for i in route_b])}")
    print("=" * 92 + "\n")

if __name__ == '__main__':
    main()