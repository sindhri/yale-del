require "csv"

PROJECT_ROOT = File.dirname(__FILE__)
DATA_DIR = "#{PROJECT_ROOT}/data"

def csv_table(filename)
  CSV.foreach("#{DATA_DIR}/#{filename}", :headers => true) do |row|
    yield row
  end
end
